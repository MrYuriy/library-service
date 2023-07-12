from django.db import models
from enum import Enum
from django.core.validators import MaxValueValidator

class BookCover(Enum):
    HARD = "Hardcover"
    SOFT = "SOFT"

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(
        max_length=10, 
        choices=[(cover.name, cover.value) for cover in BookCover]
        )
    inventory = models.IntegerField(validators=[MaxValueValidator(0)])
    dayly_fee = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.title