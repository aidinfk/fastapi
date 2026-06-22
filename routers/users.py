from models.users import User
from dependencies import SessionDep, Hasher, send_email
from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends
from sqlmodel import select
from schemas.users import UserOut, UserIn, UserUpdate, UserLogin
from jwt_auth import sign_jwt, JWTBearer


router = APIRouter()


@router.post("/users")
async def create_user(user: UserIn, session: SessionDep, background_tasks: BackgroundTasks):
    user_validate = User.model_validate(user)
    user_similar = await session.exec(select(User).where(User.email==user.email))
    if user_similar.first():
        raise HTTPException(status_code=400, detail="user with this email already exists!")
    password_hashed = Hasher.get_password_hash(user_validate.password)
    user_validate.password = password_hashed
    session.add(user_validate)
    await session.commit()
    await session.refresh(user_validate)
    background_tasks.add_task(send_email, user_validate.email)
    return sign_jwt(user_validate.email)


@router.get("/users", response_model=list[UserOut])
async def read_all_users(session: SessionDep) -> list[UserOut]:
    users = await session.exec(select(User))
    return users.all()


@router.get("/users/{user_id}", response_model=UserOut)
async def read_user(user_id: int, session: SessionDep) -> UserOut:
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found!")
    return user


@router.delete("/users/{user_id}")
async def delete_user(user_id: int, session: SessionDep, token=Depends(JWTBearer())):
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found!")
    await session.delete(user)
    await session.commit()
    return {"ok": True}


@router.patch("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserUpdate, session: SessionDep):
    user_instance = await session.get(User, user_id)
    if not user_instance:
        raise HTTPException(status_code=404, detail="user not found!")
    user_data = user.model_dump(exclude_unset=True)
    user_instance.sqlmodel_update(user_data)
    session.add(user_instance)
    await session.commit()
    await session.refresh(user_instance)
    return user_instance


@router.post("/users/login")
async def user_login(user: UserLogin, session: SessionDep):
    user_instance = await session.exec(select(User).where(User.email==user.email))
    user_instance = user_instance.first()
    if not user_instance or not Hasher.verify_password(user.password, user_instance.password):
        return HTTPException(status_code=404, detail="Email or password is wrong!")
    return sign_jwt(user_instance.email)
