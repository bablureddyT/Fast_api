from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(String(9), unique=True)
    age: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150))