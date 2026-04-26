from django.db import models

class Car(models.Model):
    BRAND_CHOICES = [
        ('TOYOTA', 'Toyota'),
        ('VOLKSWAGEN', 'Volkswagen'),
        ('FORD', 'Ford'),
        ('BMW', 'BMW'),
        ('MERCEDES', 'Mercedes-Benz'),
        ('AUDI', 'Audi'),
        ('OPEL', 'Opel'),
        ('HYUNDAI', 'Hyundai'),
        ('KIA', 'Kia'),
        ('RENAULT', 'Renault'),
    ]

    brand = models.CharField(max_length=50,
                             choices=BRAND_CHOICES)

    MODEL_CHOICES = [
        ('COROLLA', 'Corolla'),
        ('GOLF', 'Golf'),
        ('ASTRA', 'Astra'),
        ('FOCUS', 'Focus'),
        ('3SERIES', '3 Series'),
        ('A4', 'A4'),
        ('SPORTAGE', 'Sportage'),
        ('TUCSON', 'Tucson'),
        ('MEGANE', 'Megane'),
        ('C-CLASS', 'C-Class'),
    ]

    model = models.CharField(max_length=100,
                             choices=MODEL_CHOICES)

    CATEGORY_CHOICES = [
        ('ECONOMY', 'Economy'),
        ('COMPACT', 'Compact'),
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('VAN', 'Van'),
        ('LUXURY', 'Luxury'),
        ('SPORTS', 'Sports Car'),
        ('ELECTRIC', 'Electric'),
    ]

    category = models.CharField(max_length=50,
                                choices=CATEGORY_CHOICES)
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
        return f"{self.get_brand_display()} {self.get_model_display()} ({self.get_status_display()})"