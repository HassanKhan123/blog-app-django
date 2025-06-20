from django.contrib import admin
from .models import Post, Author, Tag, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date', 'author')

    list_filter = ('date', 'author', "tags")


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
