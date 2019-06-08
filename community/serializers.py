from .models import Post, Comment, User
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = (
        'auth',
        'title',
        'genre',
        'text',
        'create_dt',
        'update_dt',
    )


class CommentSerializer(serializers.ModelSerializer):
    model = Comment
    fields = (
        'post_id',
        'comment_text',
        'create_dt',
    )