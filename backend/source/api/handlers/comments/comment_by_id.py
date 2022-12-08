from source.database.models import Comment
from source.schemas.comments import CommentResponse


async def handle_get_comment(comment_id: int) -> CommentResponse:
    return await CommentResponse.from_queryset_single(Comment.get(id=comment_id))
