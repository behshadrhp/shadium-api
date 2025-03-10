import uuid

from django.db import models


class BaseModel(models.Model):

    # initial fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    # created - updated time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
