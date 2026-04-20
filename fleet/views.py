from rest_framework import viewsets
from fleet.models import Car

class CarViewSet(viewsets.ReadOnlyModelViewSet):
    """
        Listing all cars.
    """
    queryset = Car.objects.all()

