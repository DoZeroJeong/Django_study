from django.urls import path
from .views import *

restaurant = RestaurantView.as_view({'get': 'list'})


urlpatterns = [
    path('', restaurant, name='out-apply'),
]