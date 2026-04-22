from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    year = models.IntegerField()

    vin = models.CharField(max_length=17,
                           unique=True)
    license_plate = models.CharField(max_length=15,
                                     unique=True)
    color = models.CharField(max_length=50)

    daily_rate = models.DecimalField(max_digits=10,
                                     decimal_places=2)

    status = models.CharField(max_length=30,
                              default='AB',
                              choices=[('AB','AVAILABLE'),
                                        ('UR','UNDER REPAIR'),
                                        ('DS', 'DISCONTINUED')])

    def __str__(self):
        return f"{self.brand} {self.model} {self.status}"