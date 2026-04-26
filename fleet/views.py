from rest_framework import viewsets, filters
from fleet.models import Car
from fleet.serializers import CarSerializer
from fleet.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CarViewSet(viewsets.ModelViewSet):
    """
        Listing all cars.
        Guests can only use GET method.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter]
    filterset_fields  = ['brand', 'model', 'category', 'status']
    ordering_fields = ['daily_rate']