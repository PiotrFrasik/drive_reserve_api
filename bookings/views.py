from rest_framework import viewsets
from bookings.models import Booking
from bookings.serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated


class BookingViewSet(viewsets.ModelViewSet):
    """
            Listing all bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # admin can see all
        # normal user can see only own bookings
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
