from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from source.database.models import Post


class PostCreatePayload(BaseModel):
    title: str
    content: str
    description: str


PostResponse = pydantic_model_creator(
    Post,
    name="PostResponse",
    exclude=[
        "modified_at",
        "author.password",
        "author.created_at",
        "author.modified_at",
    ],
)


class PostPayloadUpdate(BaseModel):
    title: str
    content: str
    description: str
