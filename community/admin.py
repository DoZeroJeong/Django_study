from django.contrib import admin
from .models import Post, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'genre', 'create_dt', 'update_dt']
    raw_id_fields = ['author']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_text']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)