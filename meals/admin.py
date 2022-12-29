from django.contrib import admin
from .models import Testimonial, Feature, Newsletter
from django.utils.html import format_html

# Register your models here.


class TestimonialAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        try:
            return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))
        except:
            pass
    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'name')
    list_display_links = ('name', 'thumbnail')


admin.site.register(Feature)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Newsletter)