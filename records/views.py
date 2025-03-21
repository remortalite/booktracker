from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Record
from .forms import RecordForm


class RecordDetailView(DetailView):
    model = Record
    template_name = 'records/detail.html'
    context_object_name = 'record'
    pk_url_kwarg = 'record_id'


class RecordListView(ListView):
    model = Record
    template_name = 'records/list.html'
    context_object_name = 'records'


class RecordCreateView(CreateView):
    form_class = RecordForm
    success_url = reverse_lazy('record_list')
    template_name = 'records/form.html'


class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy('record_list')
    template_name = 'records/form.html'
    pk_url_kwarg = 'record_id'


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('record_list')
    template_name = 'records/confirm_delete.html'
    pk_url_kwarg = 'record_id'
