from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        try:
            return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))
        except:
            pass

    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'category',
                    'title', 'author')
    list_display_links = ('id', 'title', 'thumbnail')
    search_fields = ('title', 'writer', 'body')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)