from django.contrib import admin

from .models import Shelf


class ShelfAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    list_display_links = ['name']
    search_fields = ['name', 'book', 'user']


admin.site.register(Shelf, ShelfAdmin)
