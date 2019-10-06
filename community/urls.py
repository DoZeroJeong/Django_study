from django.urls import path
from .views import *

urlpatterns = [
    path('', PostView.as_view()),
    path('<int:pk>', PostDetailView.as_view()),
    path('<int:pk>/comment', CommentView.as_view()),
    path('<int:pk>/like', LikeView.as_view()),
]
