from django import forms
from .models import Post, Comment
from django.utils.translation import ugettext_lazy as _
# 공과대학, College of Engineering
# 소프트웨어융합대학
# 경영대학 College of Business Administration
# 보건복지교육대학 College of Health, Welfare and Education
# 건축 디자인 대학 College of Architecture and Design
# 인문사회대학 College of Humanities and Social Sciences
Options = [
    ('Free', '자유게시판'),
    ('Engineering', '공과대학게시판'),
    ('Administration', '경영대학게시판'),
    ('Health', '보건복지교육대학게시판'),
    ('Architecture', '건축디자인대학게시판'),
    ('SocialSciences', '인문사회대학게시판'),
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