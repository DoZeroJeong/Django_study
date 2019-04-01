from django.contrib import admin
from .models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'genre', 'create_dt', 'update_dt']
    raw_id_fields = ['author']


admin.site.register(Post, PostAdmin)