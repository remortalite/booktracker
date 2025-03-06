from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']
    list_display_links = ['name']
    search_fields = ['name', 'author']


admin.site.register(Book, BookAdmin)
