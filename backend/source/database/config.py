from source.core.settings import settings

TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URI},
    "apps": {
        "models": {
            "models": ["source.database.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}
