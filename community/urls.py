from django.urls import path

from .views import *

urlpatterns = [
    path('', post_index, name='post_index'),
    path('<str:genre>', post_list, name='post_list'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('update/<int:pk>/', PostUpdateVIew.as_view(), name='post_update'),
]

