from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = (
        ("F", "Fuit"),
        ("V", "Vegetable"),
        ("M", "Meat"),
        ("O", "Other"),
    )
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
