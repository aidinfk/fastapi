from sqlmodel import Field, SQLModel, Relationship


class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str

    user_id: int = Field(foreign_key="user.id", ondelete="CASCADE")
    author: "User" = Relationship(back_populates="posts", sa_relationship_kwargs={"lazy":"selectin"})