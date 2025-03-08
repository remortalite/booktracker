from django.contrib import admin

from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'status', 'created_at', 'updated_at']
    list_display_links = ['id']
    search_fields = ['book__name', 'book__author']


admin.site.register(Record, RecordAdmin)
