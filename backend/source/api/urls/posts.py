from fastapi import APIRouter, Depends, HTTPException
from tortoise.exceptions import DoesNotExist

from source.api.handlers.posts.all_posts import handle_get_all_posts
from source.api.handlers.posts.create_post import handle_create_post
from source.api.handlers.posts.delete_post import handle_delete_post
from source.api.handlers.posts.post_by_id import handle_get_post
from source.api.handlers.posts.update_post import handle_update_post
from source.schemas.posts import PostResponse, PostCreatePayload, PostPayloadUpdate
from source.schemas.users import UserResponse
from source.services.utils.jwt import get_login_user

router = APIRouter()


@router.get("/posts")
async def get_posts():
    return await handle_get_all_posts()


@router.get("/post/{post_id}", )
async def get_note(post_id: int) -> PostResponse:
    try:
        return await handle_get_post(post_id)
    except DoesNotExist:
        raise HTTPException(404, "Post dont exist")


@router.post("/posts")
async def create_posts(
        post: PostCreatePayload, user: UserResponse = Depends(get_login_user)
) -> PostResponse:
    return await handle_create_post(post, user)


@router.post("/post/{post_id}")
async def update_post(
        post_id: int,
        post: PostPayloadUpdate,
        user: UserResponse = Depends(get_login_user),
) -> PostResponse:
    return await handle_update_post(post_id, post, user)


@router.delete("/post/{post_id}")
async def delete_post(post_id: int, user: UserResponse = Depends(get_login_user)):
    return await handle_delete_post(post_id, user)
