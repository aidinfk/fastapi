from sqlmodel import SQLModel, Field, Relationship
from models.posts import Post


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str
    password: str
    age: int

    posts: list["Post"] = Relationship(cascade_delete=True, back_populates="author")