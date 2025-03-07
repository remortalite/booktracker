from django.contrib import admin

from .models import Book, Record


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']
    list_display_links = ['name']
    search_fields = ['name', 'author']


class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'status', 'created_at', 'updated_at']
    list_display_links = ['id']
    search_fields = ['book']


admin.site.register(Book, BookAdmin)
admin.site.register(Record, RecordAdmin)
