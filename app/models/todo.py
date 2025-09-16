from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, Date, ForeignKey, Boolean
from ..db import Base

class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    due_date: Mapped[str | None] = mapped_column(String(10), nullable=True)  # YYYY-MM-DD (簡易)
    done: Mapped[bool] = mapped_column(Boolean, default=False)

    owner_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    owner: Mapped["User | None"] = relationship(back_populates="todos")
