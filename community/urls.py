from django.urls import path

from .views import *

urlpatterns = [
    path('', post_index, name='post-index'),
    path('<str:genre>', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('update/<int:pk>/', PostUpdateVIew.as_view(), name='post-update'),
    path('detail/<int:pk>/', post_detail, name='post-detail'),
]
