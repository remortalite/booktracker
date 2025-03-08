from django.urls import path

from .views import RecordListView, RecordCreateView, RecordUpdateView


urlpatterns = [
    path('', RecordListView.as_view(), name='record_list'),
    path('create/', RecordCreateView.as_view(), name='record_create'),
    path('<int:record_id>/update/', RecordUpdateView.as_view(),
         name='record_update'),
]
