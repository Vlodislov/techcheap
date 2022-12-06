from source.database.models import Post
from source.schemas.posts import PostResponse
from source.schemas.response.token import StatusResponse
from tortoise.exceptions import DoesNotExist
from fastapi import HTTPException


async def handle_delete_post(post_id, user) -> StatusResponse:
    try:
        db_post = await PostResponse.from_queryset_single(Post.get(id=post_id))
    except DoesNotExist:
        raise HTTPException(404, f"Post {post_id} not found")

    if db_post.author.id == user.id:
        deleted_count = await Post.filter(id=post_id).delete()
        if not deleted_count:
            raise HTTPException(404, f"Post {post_id} not found")
        return StatusResponse(message=f"Deleted post {post_id}")

    raise HTTPException(403, f"Not authorized")
