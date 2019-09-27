from django.urls import path
from .views import *

urlpatterns = [
    path('', OutApply.as_view(), name='out-apply'),
]