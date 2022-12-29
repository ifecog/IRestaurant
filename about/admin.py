from django.contrib import admin
from .models import Chef, About
from django.utils.html import format_html

# Register your models here.


class ChefAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'name', 'role')
    list_display_links = ('id', 'name', 'thumbnail')
    search_fields = ('name', 'role')


admin.site.register(Chef, ChefAdmin)
admin.site.register(About)
