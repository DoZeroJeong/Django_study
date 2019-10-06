from .models import Post, Comment, Like
from rest_framework import serializers
from django.contrib.auth.models import User

Options = [
    ('Free', '자유게시판'),
    ('Engineering', '공과대학게시판'),
    ('Administration', '경영대학게시판'),
    ('Health', '보건복지교육대학게시판'),
    ('Architecture', '건축디자인대학게시판'),
    ('SocialSciences', '인문사회대학게시판'),
    ('Market', '중고장터게시판'),
]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
        )


class CommentSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'author',
            'comment_text',
        )


class LikeSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = (
            'id',
            'author',
        )


class PostSerializer(serializers.ModelSerializer):

    genre = serializers.ChoiceField(choices=Options)
    author = UserSerializer(read_only=True)
    comment = CommentSerializer(many=True, read_only=True)
    like = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'author',
            'title',
            'genre',
            'file',
            'text',
            'create_dt',
            'update_dt',
            'comment',
            'like',
        )