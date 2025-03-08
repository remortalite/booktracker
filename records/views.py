from django.views.generic.list import ListView

from .models import Record


class RecordListView(ListView):
    model = Record
    template_name = 'records/list.html'
    context_object_name = 'records'
