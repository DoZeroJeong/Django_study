from django.shortcuts import render
from .models import Tu_Data
from .forms import TuDataForm
from .selenium_test import dormitory
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DormitorySerializer
from rest_framework import status, viewsets

# Create your views here.

# @api_view(['GET', 'PUT', 'POST'])
# def out_apply(request):
#     if request.method == "POST":
#         tu_form = TuDataForm(request.POST)
#         serializer = DormitorySerializer()
#         if tu_form.is_valid():
#             tu_id = serializer.get_fields("tu_id")
#             tu_password = serializer.get_fields("tu_password")
#             first_day = serializer.get_fields("first_day")
#             second_day = serializer.get_fields("second_day")
#             apply_text = serializer.get_fields("apply_text")
#             dormitory(tu_id, tu_password, first_day, second_day, apply_text)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == "GET":
#         serializer = DormitorySerializer()
#         return Response(serializer.data, template_name='dormitory/apply.html')
#     return Response(DormitorySerializer().data, status=status.HTTP_200_OK, template_name='dormitory/apply.html')


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





