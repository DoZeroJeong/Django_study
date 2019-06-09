from .models import Tu_Data
from .selenium_test import dormitory
from .serializers import DormitorySerializer
from rest_framework import viewsets


class OutApply(viewsets.ModelViewSet):
    queryset = Tu_Data.objects.all()
    serializer_class = DormitorySerializer

    def perform_create(self, serializer):
        tu_id = serializer.data.get("tu_id")
        tu_password = serializer.data.get("tu_password")
        first_day = serializer.data.get("first_day")
        second_day = serializer.data.get("second_day")
        apply_text = serializer.data.get("apply_text")
        dormitory(tu_id, tu_password, first_day, second_day, apply_text)

