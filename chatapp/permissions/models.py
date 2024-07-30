from django.db import models
from django.contrib.contenttypes.models import ContentType
from base.models import BaseModel

content_types = ContentType.objects.all()


class Permission(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
