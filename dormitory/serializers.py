from .models import Tu_Data
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

class DormitorySerializer(serializers.ModelSerializer):
    tu_password = serializers.CharField(
        style={'input_type': 'password'}
    )

    class Meta:
        model = Tu_Data
        fields = [
            'tu_id',
            'tu_password',
            'first_day',
            'second_day',
            'apply_text',
        ]