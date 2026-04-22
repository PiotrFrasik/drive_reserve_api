from rest_framework import viewsets
from fleet.models import Car
from fleet.serializers import CarSerializer


class CarViewSet(viewsets.ReadOnlyModelViewSet):
    """
        Listing all cars.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
