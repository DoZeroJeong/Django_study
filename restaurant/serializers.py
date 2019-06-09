from rest_framework import serializers
from .models import Restaurant_Data


class RestaurantSerializer(serializers.ModelSerializer):
    student_menu = serializers.FilePathField
    faculty_menu = serializers.FilePathField

    class Meta:
        model = Restaurant_Data
        fields = (
            'student_menu',
            'faculty_menu',
        )

