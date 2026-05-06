from rest_framework import serializers
from reviews.models import Review
from bookings.models import Booking

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, data):
        # user can add review after booking is completed
        booking_exists = Booking.objects.filter(
            user=self.context['request'].user,
            car=data.get('car'),
            status='COM'
        ).exists()

        if not booking_exists:
            raise serializers.ValidationError({'booking_status':'You nust have a completed booking to leave a review'})

        # user can't add another review for the same car
        review_exists = Review.objects.filter(
            user=self.context['request'].user,
            car=data.get('car'),
        ).exists()

        if review_exists:
            raise serializers.ValidationError({'review_status':'You have already reviewed this car'})

        return data