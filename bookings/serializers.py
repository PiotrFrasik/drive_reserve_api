import datetime

from rest_framework import serializers, status
from bookings.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        current_date = datetime.date.today()

        # validate date
        if data.get('start_date') < current_date:
            raise serializers.ValidationError({'start_date':'Start date cannot be in the past'})

        if data.get('end_date') <= data.get('start_date'):
            raise serializers.ValidationError({'end_date':'End date cannot be after start date'})

        # accessibility logic
        conflict_bookings = Booking.objects.filter(
            car = data['car'],
            start_date__lt=data['end_date'],
            end_date__gt=data['start_date']
        ).exclude(status='CAN')

        if conflict_bookings.exists():
            raise serializers.ValidationError({'conflict_bookings':'This car already booking'})

        # check car status
        if data['car'].status != 'AB':
            raise serializers.ValidationError({'status':'This car is inaccessible'})

        #  price calculation
        duration = data['end_date'] - data['start_date']
        days = duration.days

        if days < 0:
            raise serializers.ValidationError({'end_date':'End date cannot be after current date'})

        data['total_price'] = days * data['car'].daily_rate

        return data