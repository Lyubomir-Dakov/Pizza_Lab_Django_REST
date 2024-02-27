from django.db import models


class Employee(models.Model):
    name = models.CharField(
        max_length=50
    )

    position = models.CharField(
        max_length=50
    )

    restaurant = models.ForeignKey(
        "restaurants.Restaurant",
        on_delete=models.RESTRICT,
        related_name="employees",  # This specifies the reverse relation name
    )

    def __str__(self):
        return self.name
