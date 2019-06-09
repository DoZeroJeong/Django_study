from .models import Tu_Data
from rest_framework import serializers


class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tu_Data
        fields = (
            'tu_id',
            'tu_password',
            'first_day',
            'second_day',
            'apply_text',
        )