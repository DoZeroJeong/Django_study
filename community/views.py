from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


class PostView(GenericAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
