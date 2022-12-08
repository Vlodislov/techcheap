from source.database.models import Comment
from source.schemas.comments import CommentResponse
from tortoise.exceptions import DoesNotExist
from fastapi import HTTPException


async def handle_update_comment(comment_id: int, comment, user) -> CommentResponse:
    try:
        db_comment = await CommentResponse.from_queryset_single(
            Comment.get(id=comment_id)
        )
    except DoesNotExist:
        raise HTTPException(404, f"Comment {comment_id} not found")

    if db_comment.author.id == user.id:
        await Comment.filter(id=comment_id).update(**comment.dict(exclude_unset=True))
        return await CommentResponse.from_queryset_single(Comment.get(id=comment_id))

    raise HTTPException(403, f"Not authorized")
