from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    avatar = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return str(self.username)

    def to_dict_json(user):
        d = {
            "id": user.id,
            "name": user.get_full_name(),
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "avatar": user.avatar,
            "bio": user.bio,
            "permissions": {
                "ADMIN": user.is_superuser,
                "STAFF": user.is_staff,
            },
        }
        return d
