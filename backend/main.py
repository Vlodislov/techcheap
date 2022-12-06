from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from source.database.core import core_tortoise
from source.database.config import TORTOISE_ORM

# enable schemas to read relationship between models
Tortoise.init_models(["source.database.models"], "models")

from source.api.urls import users, posts

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(posts.router)

core_tortoise(app, config=TORTOISE_ORM, gen_schemas=False)


@app.get("/")
def home():
    return "Hello, World!"
