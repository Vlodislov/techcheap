from source.database.models import Post
from source.schemas.posts import PostResponse


async def handle_get_post(post_id) -> PostResponse:
    return await PostResponse.from_queryset_single(Post.get(id=post_id))
