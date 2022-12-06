from source.database.models import User
from source.schemas.response.token import StatusResponse
from tortoise.exceptions import DoesNotExist
from fastapi import HTTPException

from source.schemas.users import UserResponse


async def handle_delete_user(user_id, user) -> StatusResponse:
    try:
        db_user = await UserResponse.from_queryset_single(User.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(404, f"User {user_id} not found")

    if db_user.id == user.id:
        deleted_count = await User.filter(id=user_id).delete()
        if not deleted_count:
            raise HTTPException(404, f"User {user_id} not found")
        return StatusResponse(message=f"Deleted user {user_id}")

    raise HTTPException(403, f"Not authorized")
