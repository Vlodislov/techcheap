from pydantic.main import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from source.database.models import User


class UserCreatePayload(BaseModel):
    login: str
    password: str
    nickname: str
    email: str


UserResponse = pydantic_model_creator(
    User, name="UserResponse", exclude=["password", "created_at", "modified_at"]
)
UserDatabase = pydantic_model_creator(
    User, name="User", exclude=["created_at", "modified_at"]
)
