from django.urls import path
from django.views.generic.detail import DetailView

from .views import *
from .models import Post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('detail/<int:pk>/', DetailView.as_view(model=Post, template_name='community/detail.html'), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('update/<int:pk>/', PostUpdateVIew.as_view(), name='post_update'),
]

