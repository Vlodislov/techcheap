from source.database.models import Post
from source.schemas.posts import PostResponse


async def handle_create_post(post, user) -> PostResponse:
    post_dict = post.dict(exclude_unset=True)
    post_dict["author_id"] = user.id
    post = await Post.create(**post_dict)
    return await PostResponse.from_tortoise_orm(post)
