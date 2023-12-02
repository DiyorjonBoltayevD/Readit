from django.contrib import admin

from blog.models import *


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created']
    list_display_links = ['title', 'description']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'created']
