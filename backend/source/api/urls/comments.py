from fastapi import APIRouter, Depends, HTTPException
from tortoise.exceptions import DoesNotExist

from source.api.handlers.comments.all_comments import handle_get_all_comments
from source.api.handlers.comments.comment_by_id import handle_get_comment
from source.api.handlers.comments.create_comment import handle_create_comment
from source.api.handlers.comments.delete_comment import handle_delete_comment
from source.api.handlers.comments.update_comment import handle_update_comment
from source.schemas.comments import (
    CommentResponse,
    CommentCreatePayload,
    CommentPayloadUpdate,
)
from source.schemas.users import UserResponse
from source.services.utils.jwt import get_login_user

router = APIRouter()


@router.get("/comments")
async def get_comment():
    return await handle_get_all_comments()


@router.get("/comments/{comment_id}")
async def get_comment(comment_id: int) -> CommentResponse:
    try:
        return await handle_get_comment(comment_id)
    except DoesNotExist:
        raise HTTPException(404, "Comment dont exist")


@router.post("/comments")
async def create_comment(
        comment: CommentCreatePayload,
        post_id: int,
        user: UserResponse = Depends(get_login_user),
) -> CommentResponse:
    return await handle_create_comment(comment, post_id, user)


@router.post("/comments/{comment_id}")
async def update_comment(
        comment_id: int,
        comment: CommentPayloadUpdate,
        user: UserResponse = Depends(get_login_user),
) -> CommentResponse:
    return await handle_update_comment(comment_id, comment, user)


@router.delete("/comments/{comment_id}")
async def delete_comment(comment_id: int, user: UserResponse = Depends(get_login_user)):
    return await handle_delete_comment(comment_id, user)
