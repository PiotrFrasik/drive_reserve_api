from rest_framework import viewsets
from bookings.models import Booking
from bookings.serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

