from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

# 게시글 리스트
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

# 게시글 상세보기
class PostDetailView(APIView):

    serializer_class = PostSerializer

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(data=serializer.data)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentView(GenericAPIView):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def post(self, request, pk):
        post_id = Post.objects.get(pk=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post_id=post_id)
            return Response(data=serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        comment_id = Comment.objects.filter(pk=pk)
        comment_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LikeView(GenericAPIView):

    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def post(self, request, pk):
        post_id = Post.objects.get(pk=pk)
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                pass
            except Like.DoesNotExit:
                serializer.save(author=request.user, post_id=post_id)
                return Response(data=serializer.data)
        return Response(serializer.errors)

