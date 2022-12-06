from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist

from source.database.models import User
from source.schemas.users import UserDatabase

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def get_user(username: str):
    return await UserDatabase.from_queryset_single(User.get(login=username))


async def validate_user(user: OAuth2PasswordRequestForm = Depends()):
    try:
        db_user = await get_user(user.username)
    except DoesNotExist:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Incorrect login or password",
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Incorrect login or password",
        )

    return db_user
