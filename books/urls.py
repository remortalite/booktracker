from django.urls import path

from .views import IndexPageView, BookListView, BookDetailView


urlpatterns = [
    path('', IndexPageView.as_view(), name='index_page'),
    path('list/', BookListView.as_view(), name='books_list'),
    path('book/<int:book_id>/', BookDetailView.as_view(), name='book_detail'),
]
