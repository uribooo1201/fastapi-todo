from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..db import get_db
from ..models.todo import Todo
from ..schemas.todo import TodoCreate, TodoUpdate, TodoOut

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("", response_model=TodoOut, status_code=status.HTTP_201_CREATED)
def create_todo(payload: TodoCreate, db: Session = Depends(get_db)):
    todo = Todo(**payload.dict())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

@router.get("", response_model=list[TodoOut])
def list_todos(db: Session = Depends(get_db), q: str | None = None, done: bool | None = None):
    query = db.query(Todo)
    if q:
        query = query.filter(Todo.title.ilike(f"%{q}%"))
    if done is not None:
        query = query.filter(Todo.done == done)
    return query.order_by(Todo.id.desc()).all()

@router.get("/{todo_id}", response_model=TodoOut)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoOut)
def update_todo(todo_id: int, payload: TodoUpdate, db: Session = Depends(get_db)):
    todo = db.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for k, v in payload.dict(exclude_unset=True).items():
        setattr(todo, k, v)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return None
