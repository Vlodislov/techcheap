from datetime import timedelta, datetime

from fastapi.security import OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi import Request, HTTPException, Depends
from fastapi.security.utils import get_authorization_scheme_param
from jose import JWTError, jwt
from tortoise.exceptions import DoesNotExist

from source.core.settings import settings
from source.database.models import User
from source.schemas.response.token import TokenResponse
from source.schemas.users import UserResponse

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class OAuth2PasswordBearerCookie(OAuth2):
    def __init__(
        self,
        token: str,
        scheme_name: str = None,
        scopes: dict = None,
        auto_error: bool = None,
    ):
        if not scopes:
            scopes = {}
        auth_flows_model = OAuthFlowsModel(
            password={"tokenUrl": token, "scopes": scopes}
        )
        super().__init__(
            flows=auth_flows_model, scheme_name=scheme_name, auto_error=auto_error
        )

    async def __call__(self, request: Request) -> str:
        authorization: str = request.cookies.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)

        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(401, "Not authenticated")
            else:
                return None

        return param


security = OAuth2PasswordBearerCookie(token="/login")


def handle_create_access_toke(data: dict, expires_delta: timedelta = None):
    data_to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    data_to_encode.update({"exp": expire})
    token_encoded = jwt.encode(data_to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)

    return token_encoded


async def get_login_user(token: str = Depends(security)):
    try:
        print(token)
        token_decode = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        login: str = token_decode.get("sub")
        if login is None:
            raise HTTPException(401, "Could not validate credentials")
        token_response = TokenResponse(login=login)
    except JWTError:
        raise HTTPException(401, "Could not validate credentials")

    try:
        user = await UserResponse.from_queryset_single(
            User.get(login=token_response.login)
        )
    except DoesNotExist:
        raise HTTPException(401, "Could not validate credentials")

    return user
