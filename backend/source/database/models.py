from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    login = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)
    nickname = fields.CharField(max_length=50, null=True)
    email = fields.CharField(max_length=50, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)


class Post(models.Model):
    id = fields.IntField(pk=True)
    author = fields.ForeignKeyField("models.User", related_name="post")
    title = fields.CharField(max_length=225)
    content = fields.TextField()
    description = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Comment(models.Model):
    id = fields.IntField(pk=True)
    author = fields.ForeignKeyField("models.User", related_name="author")
    post = fields.ForeignKeyField("models.Post", related_name="post")
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
