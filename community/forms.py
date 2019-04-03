from django import forms
from .models import Post, Comment
from django.utils.translation import ugettext_lazy as _

Options = [
    ('Free', '자유게시판'),
    ('Subject', '학과별게시판'),
    ('Market', '중고장터게시판'),
]


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'genre', 'text']
        widgets = {
            'genre': forms.Select(choices=Options)
        }
        labels = {
            'title': _('제목'),
            'genre': _('게시판'),
            'text': _('내용'),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post_id', 'comment_text']
        labels = {
            'comment_text': _('댓글'),
        }
        widgets = {
            'post_id': forms.HiddenInput()
        }