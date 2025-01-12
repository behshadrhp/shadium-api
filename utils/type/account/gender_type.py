from django.db import models


class GenderType(models.TextChoices):

    Male = "male", "Male"
    Female = "female", "Female"
