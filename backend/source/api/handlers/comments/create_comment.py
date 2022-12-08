from source.database.models import Comment
from source.schemas.comments import CommentResponse


async def handle_create_comment(comment, post_id: int, user) -> CommentResponse:
    comment_dict = comment.dict(exclude_unset=True)
    comment_dict["author_id"] = user.id
    comment_dict["post_id"] = post_id
    comment = await Comment.create(**comment_dict)
    return await CommentResponse.from_tortoise_orm(comment)
