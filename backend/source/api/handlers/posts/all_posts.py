from source.database.models import Post
from source.schemas.posts import PostResponse


async def handle_get_all_posts() -> PostResponse:
    return await PostResponse.from_queryset(Post.all())
