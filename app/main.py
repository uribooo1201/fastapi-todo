from fastapi import FastAPI
from .api.todos import router as todos_router
from .db import Base, engine

app = FastAPI(title="FastAPI ToDo")

# 開発容易化のため、自動でテーブル作成（本番はAlembicを推奨）
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print("DB init warning:", e)

app.include_router(todos_router)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
