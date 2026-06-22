from fastapi import APIRouter, HTTPException, Depends
from schemas.posts import PostIn, PostOut
from models.posts import Post
from models.users import User
from dependencies import SessionDep
from sqlmodel import select
from jwt_auth import JWTBearer, decode_jwt



router = APIRouter()

@router.post("/create-post", response_model=PostOut)
async def create_post(post: PostIn, session: SessionDep, token=Depends(JWTBearer())):
    user_identifier = str(decode_jwt(token)["user_identifier"])
    user = await session.exec(select(User).where(User.email==user_identifier))
    user_instance = await session.exec(select(User).where(User.id==user.first().id))
    if not user_instance:
        raise HTTPException(status_code=400, detail="User with this id does not exists!")
    post_instance = Post(title=post.title, description=post.description, author=user_instance.first())
    session.add(post_instance)
    await session.commit()
    await session.refresh(post_instance)
    return post_instance


@router.get("/read-post/{post_id}")
async def read_post(post_id: int, session: SessionDep):
    result = await session.exec(select(Post).where(Post.id==post_id))
    post = result.first()
    return post


@router.delete("/delete-post/{post_id}")
async def delete_post(post_id: int, session: SessionDep, token=Depends(JWTBearer())):
    user_identifier = str(decode_jwt(token)["user_identifier"])
    user_instance = await session.exec(select(User).where(User.email==user_identifier))
    user = user_instance.first()
    post_instance = await session.exec(select(Post).where(Post.id==post_id))
    post = post_instance.first()
    if not user.id == post.author.id:
        raise HTTPException(status_code=403, detail="Permission denied, you are not the owner of this post!")
    await session.delete(post)
    await session.commit()
    return {"ok": True}