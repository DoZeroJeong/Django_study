from rest_framework import serializers
from .models import Restaurant_Data


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_Data
        fields = (
            'ddoock',
            'il',
            'rice',
            'noodle',
            'yang',
            'faculty_menu',
        )

