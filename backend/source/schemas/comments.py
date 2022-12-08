from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from source.database.models import Comment


class CommentCreatePayload(BaseModel):
    content: str


CommentResponse = pydantic_model_creator(
    Comment,
    name="CommentResponse",
    exclude=[
        "modified_at",
        "author.password",
        "author.created_at",
        "author.modified_at",
        "post.created_at",
        "post.modified_at",
    ],
)


class CommentPayloadUpdate(BaseModel):
    content: str
