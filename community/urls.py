from django.urls import path

from .views import *

urlpatterns = [
    path('', post_index, name='post-index'),
    path('<str:genre>', post_list, name='post-list'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('update/<int:pk>/', PostUpdateVIew.as_view(), name='post-update'),
]

