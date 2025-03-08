from django.urls import path

from .views import IndexPageView, BooksView


urlpatterns = [
    path('', IndexPageView.as_view(), name='index_page'),
    path('list/', BooksView.as_view(), name='books_list'),
]
