from rest_framework import viewsets
from bookings.models import Booking

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()

