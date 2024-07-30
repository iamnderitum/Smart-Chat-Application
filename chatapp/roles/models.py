from django.db import models

from base.models import BaseModel
from permissions.models import Permission


class Role(BaseModel):
    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permission)

    def __str__(self) -> str:
        return self.name