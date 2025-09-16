import os
import pytest
from fastapi.testclient import TestClient

# Only run if DATABASE_URL points to Postgres
DB_URL = os.getenv("DATABASE_URL", "")
if not DB_URL.startswith("postgresql"):
    pytest.skip("Skipping E2E (Postgres) tests: DATABASE_URL is not Postgres.", allow_module_level=True)

from app.main import app  # noqa: E402

client = TestClient(app)

def test_e2e_crud_on_postgres():
    # ensure health
    r = client.get("/healthz")
    assert r.status_code == 200

    # list empty
    r = client.get("/todos")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

    # create
    payload = {"title": "e2e task", "description": "run against Postgres"}
    r = client.post("/todos", json=payload)
    assert r.status_code == 201
    todo = r.json()
    assert todo["title"] == payload["title"]
    todo_id = todo["id"]

    # read
    r = client.get(f"/todos/{todo_id}")
    assert r.status_code == 200
    assert r.json()["id"] == todo_id

    # update
    r = client.put(f"/todos/{todo_id}", json={"done": True})
    assert r.status_code == 200
    assert r.json()["done"] is True

    # delete
    r = client.delete(f"/todos/{todo_id}")
    assert r.status_code == 204

    # confirm
    r = client.get(f"/todos/{todo_id}")
    assert r.status_code == 404
