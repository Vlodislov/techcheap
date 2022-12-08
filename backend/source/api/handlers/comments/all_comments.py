from source.database.models import Post, Comment
from source.schemas.comments import CommentResponse


async def handle_get_all_comments() -> CommentResponse:
    return await CommentResponse.from_queryset(Comment.all())
