from pydantic import BaseModel



class UserBase(BaseModel):
    email: str
    username: str
    age: int


class UserOut(UserBase):
    id: int


class UserIn(UserBase):
    password: str


class UserUpdate(UserBase):
    email: str | None = None
    username: str | None = None
    age: int | None = None


class UserLogin(BaseModel):
    email: str
    password: str