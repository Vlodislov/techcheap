from source.database.models import Post
from source.schemas.posts import PostResponse
from tortoise.exceptions import DoesNotExist
from fastapi import HTTPException


async def handle_update_post(post_id, post, user) -> PostResponse:
    try:
        db_post = await PostResponse.from_queryset_single(Post.get(id=post_id))
    except DoesNotExist:
        raise HTTPException(404, f"Post {post_id} not found")

    if db_post.author.id == user.id:
        await Post.filter(id=post_id).update(**post.dict(exclude_unset=True))
        return await PostResponse.from_queryset_single(Post.get(id=post_id))

    raise HTTPException(403, f"Not authorized")
