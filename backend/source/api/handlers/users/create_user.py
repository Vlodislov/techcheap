from source.database.models import User
from source.schemas.users import UserResponse, UserCreatePayload
from source.services.auth.user import pwd_context
from fastapi import HTTPException
from tortoise.exceptions import IntegrityError


async def handle_create_user(user: UserCreatePayload) -> UserResponse:
    user.password = pwd_context.encrypt(user.password)
    try:
        user = await User.create(**user.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(401, "That login already exists.")
    return await UserResponse.from_tortoise_orm(user)
