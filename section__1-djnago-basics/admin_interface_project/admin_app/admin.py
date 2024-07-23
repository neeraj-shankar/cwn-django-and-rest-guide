from django.contrib import admin
from .models import Post, Tag

# Customize the action and appearance admin site
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'content', 'author')
    search_fields = ('title', 'author')
    list_filter = ('author', 'created_at')


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

