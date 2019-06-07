from django.urls import path
from .views import *

dormitory = OutApply.as_view({'post': 'create', 'get': 'list'})


urlpatterns = [
    path('', dormitory, name='out-apply'),
]