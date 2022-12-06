from typing import Optional
from tortoise import Tortoise


def core_tortoise(app, config: Optional[str] = None, gen_schemas: bool = False):
    @app.on_event("startup")
    async def start():
        await Tortoise.init(config=config)
        if gen_schemas:
            await Tortoise.generate_schemas()

    @app.on_event("shutdown")
    async def stop():
        await Tortoise.close_connections()
