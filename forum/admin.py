from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Game

# Register your models here.


class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

admin.site.register(Post, SummerAdmin)
admin.site.register(Comment, SummerAdmin)
admin.site.register(Game)
