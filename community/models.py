from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auth')
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    text = models.TextField()
    create_dt = models.DateField(auto_now_add=True)
    update_dt = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-list', kwargs={'genre': self.genre})


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    create_dt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment_text

class Like(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_cnt = models.IntegerField(default=0)
