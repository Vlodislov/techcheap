from pydantic import BaseModel


class TokenResponse(BaseModel):
    login: str = None


class StatusResponse(BaseModel):
    message: str
