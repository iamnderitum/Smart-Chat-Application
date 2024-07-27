from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_archived = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        abstract = True
