from django.db import models
from django.contrib.contenttypes.models import ContentType

content_types = ContentType.objects.all()
from base.models import BaseModel


class Permission(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


