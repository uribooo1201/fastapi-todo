from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from ..db import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)

    todos: Mapped[list["Todo"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
