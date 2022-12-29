from django.contrib import admin
from .models import Category, Menu, Booking
from django.utils.html import format_html

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        try:
            return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))
        except:
            pass
    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'name')
    list_display_links = ('name', 'thumbnail')


class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    def thumbnail(self, object):
        try:
            return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))
        except:
            pass
    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'name', 'category',
                    'price', 'preparation_time')
    list_display_links = ('name', 'thumbnail')
    search_fields = ('name', 'category')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',
                    'date', 'time', 'no_of_persons')
    list_display_links = ('name', 'email')
    search_fields = ('name', 'email')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Booking, BookingAdmin)
