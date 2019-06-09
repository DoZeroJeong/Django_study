from rest_framework import serializers
from .models import Restaurant_Data


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_Data
        fields = (
            'student_menu',
            'faculty_menu',
        )

