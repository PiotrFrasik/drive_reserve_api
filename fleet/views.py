from rest_framework import viewsets
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from fleet.models import Car
from fleet.serializers import CarSerializer
from fleet.permissions import IsAdminOrReadOnly


class CarViewSet(viewsets.ModelViewSet):
    """
        Listing all cars.
        Guests can only use GET method.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminOrReadOnly]