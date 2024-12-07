from django.contrib import admin
from .models import *

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'author', 'created_on', 'last_update']
    list_editable = ['published','author',]


admin.site.register(BlogPost, BlogPostAdmin)