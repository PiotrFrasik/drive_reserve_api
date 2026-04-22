import datetime
from rest_framework import serializers
from decimal import Decimal
from fleet.models import Car


class CarSerializer(serializers.ModelSerializer):
    #Return abbreviation
    status = serializers.CharField(source='get_status_display',
                                   read_only=True)
    #Rate for week with 10% less
    week_rate = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = '__all__'

    def validate(self, data):
        # validate date
        current_year = datetime.datetime.now().year
        if data['year'] < 2020 or data['year'] > current_year:
            raise serializers.ValidationError({"year": "Invalid year of manufacture."})

        if len(data['vin']) != 17:
            raise serializers.ValidationError({"vin": "VIN must be exactly 17 characters."})

        return data

    # promotion for week rent
    def get_week_rate(self, obj):
        """
            10% less for week rate
        """
        week_price = obj.daily_rate * 7 * Decimal('0.9')
        return round(week_price, 2)