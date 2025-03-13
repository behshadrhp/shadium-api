from django.db import models

class PostStatus(models.TextChoices):
    PB = "pb", "Public"
    DF = "df", "Draft"
