from pydantic import BaseModel


class PostIn(BaseModel):
    title: str
    description: str


class PostOut(BaseModel):
    id: int
    title: str
    description: str
    user_id: int


class PostIdIn(BaseModel):
    id: int