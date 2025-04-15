from django.db import models


class RatingType(models.TextChoices):
    poor = "poor", "Poor"
    fair = "fair", "Fair"
    good = "good", "Good"
    very_good = "very_good", "Very Good"
    excellent = "excellent", "Excellent"
    