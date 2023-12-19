from django.contrib import admin
from .models import Author, Post, Tag, PostComments

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("post_author", "post_tag", "post_date",)
    list_display = ("post_title", "post_date", "post_author",)
    prepopulated_fields = {
        "post_slug" : ("post_title",)
    }

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("tag_caption",)

@admin.register(PostComments)
class PostCommentsAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "comment", "post",)

