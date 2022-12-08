from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from source.api.handlers.users.create_user import handle_create_user
from source.api.handlers.users.delete_user import handle_delete_user
from source.schemas.response.token import StatusResponse
from source.schemas.users import UserCreatePayload, UserResponse
from source.services.auth.user import validate_user
from source.services.utils.jwt import (
    get_login_user,
    handle_create_access_toke,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

router = APIRouter()


@router.post("/register")
async def create_user(user: UserCreatePayload) -> UserResponse:
    return await handle_create_user(user)


@router.post("/login")
async def login(user: OAuth2PasswordRequestForm = Depends()):
    user = await validate_user(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = handle_create_access_toke(
        data={"sub": user.login}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    content = {"message": "Successfully logged in."}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False,
    )
    return response


@router.get("/users/iam")
async def read_users_me(current_user: UserResponse = Depends(get_login_user)):
    return current_user


@router.delete("/user/{user_id}")
async def delete_user(
    user_id: int, current_user: UserResponse = Depends(get_login_user)
) -> StatusResponse:
    return await handle_delete_user(user_id, current_user)
