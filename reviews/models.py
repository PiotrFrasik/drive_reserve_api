from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from fleet.models import Car

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Very Poor'),
        (2, '2 - Poor'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]
    # relation to car
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    # relation to user
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='reviews'
    )

    # rating 1-5
    rating = models.PositiveIntegerField(
        choices=RATING_CHOICES,
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    comment = models.TextField(max_length=500,
                               blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # one user can rate car just once
        unique_together = ('car', 'user')

    def __str__(self):
        return f"Review for {self.car} by {self.user} - {self.rating}/5"