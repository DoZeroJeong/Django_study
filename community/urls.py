from django.urls import path
from .views import PostView, CommentView

post_list = PostView.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

comment_list = CommentView.as_view({
    'get': 'list',
    'post': 'create'
})

comment_detail = CommentView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', post_list),
    path(r'<int:pk>', post_detail),
    path('comment/', comment_list),
    path('comment/<int:pk>', comment_detail),
    # path('like/', LikeView.as_view()),
]
