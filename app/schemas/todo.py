from pydantic import BaseModel, Field

class TodoBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    due_date: str | None = None
    done: bool = False
    owner_id: int | None = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    due_date: str | None = None
    done: bool | None = None

class TodoOut(TodoBase):
    id: int

    class Config:
        from_attributes = True
