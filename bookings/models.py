from django.db import models
from django.conf import settings
from fleet.models import Car as Car_Fleet

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='bookings')
    car = models.ForeignKey(Car_Fleet,
                            on_delete=models.CASCADE,
                            related_name='bookings')

    start_date = models.DateField()
    end_date = models.DateField()
    status =  models.CharField(max_length=30,
                              choices=[('PEND', 'PENDING'),
                                        ('CON', 'CONFIRMED'),
                                        ('COM', 'COMPLETED'),
                                       ('CAN', 'CANCELLED')],
                              default='PEND')

    total_price = models.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       null=True,
                                       blank=True)

    def __str__(self):
        return f"Booking {self.id} - {self.user.username} - {self.car.brand} {self.car.model}"

class Review(models.Model):
    booking = models.OneToOneField(Booking,
                                   on_delete=models.CASCADE,
                                   related_name='review')
    rating = models.IntegerField()
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='user_reviews')

    def __str__(self):
        return f"Review for Booking {self.booking.id} - Rating: {self.rating}"