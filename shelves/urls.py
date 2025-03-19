from django.urls import path

from .views import shelf_list_view, shelf_detail_view


urlpatterns = [
    path('', shelf_list_view, name='shelf_list'),
    path('<int:shelf_id>/', shelf_detail_view, name='shelf_detail'),
]
