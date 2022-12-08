from source.database.models import Comment
from source.schemas.comments import CommentResponse
from source.schemas.response.token import StatusResponse
from tortoise.exceptions import DoesNotExist
from fastapi import HTTPException


async def handle_delete_comment(comment_id: int, user) -> StatusResponse:
    try:
        db_comment = await CommentResponse.from_queryset_single(
            Comment.get(id=comment_id)
        )
    except DoesNotExist:
        raise HTTPException(404, f"Comment {comment_id} not found")

    if db_comment.author.id == user.id:
        deleted_count = await Comment.filter(id=comment_id).delete()
        if not deleted_count:
            raise HTTPException(404, f"Comment {comment_id} not found")
        return StatusResponse(message=f"Deleted comment {comment_id}")

    raise HTTPException(403, f"Not authorized")
