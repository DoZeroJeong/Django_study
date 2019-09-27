from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *


urlpatterns = [
    path('', UserList.as_view(), name='account-list'),
    path('<int:pk>', UserDetail.as_view(), name='account-detail'),
]