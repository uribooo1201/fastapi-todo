from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db import Base, get_db

# Use a file-based SQLite for stability across multiple connections in tests
TEST_DB_URL = "sqlite:///./test_ci.db"

engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables for tests
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override the app's DB dependency
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_todos_crud_flow():
    # List (empty)
    r = client.get("/todos")
    assert r.status_code == 200
    assert r.json() == []

    # Create
    payload = {"title": "write tests", "description": "pytest + GitHub Actions"}
    r = client.post("/todos", json=payload)
    assert r.status_code == 201
    todo = r.json()
    assert todo["title"] == payload["title"]
    todo_id = todo["id"]

    # Get
    r = client.get(f"/todos/{todo_id}")
    assert r.status_code == 200
    assert r.json()["id"] == todo_id

    # Update
    r = client.put(f"/todos/{todo_id}", json={"done": True})
    assert r.status_code == 200
    assert r.json()["done"] is True

    # Filter by done
    r = client.get("/todos", params={"done": True})
    assert r.status_code == 200
    data = r.json()
    assert any(t["id"] == todo_id for t in data)

    # Delete
    r = client.delete(f"/todos/{todo_id}")
    assert r.status_code == 204

    # Confirm deletion
    r = client.get(f"/todos/{todo_id}")
    assert r.status_code == 404
