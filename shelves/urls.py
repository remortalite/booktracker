from django.urls import path

from .views import (shelf_list_view, shelf_detail_view,
                    shelf_create_view, shelf_update_view)


urlpatterns = [
    path('', shelf_list_view, name='shelf_list'),
    path('create/', shelf_create_view, name='shelf_create'),
    path('<int:shelf_id>/', shelf_detail_view, name='shelf_detail'),
    path('<int:shelf_id>/update', shelf_update_view, name='shelf_update'),
]
