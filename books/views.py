from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages

from .models import Book
from .forms import BookForm


class IndexPageView(View):
    def get(self, request):
        return render(request, 'index.html')


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/list.html', {'books': books})


class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'books/detail.html', {'book': book})


class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'books/create.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('books_list'))
        return render(request, 'books/create.html', {'form': form})


class BookUpdateView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        form = BookForm(instance=book)
        return render(request, 'books/update.html', {'form': form})

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('books_list'))
        return render(request, 'books/update.html', {'form': form})


class BookDeleteView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'books/delete.html', {'book': book})

    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if book.record_set.exists():
            messages.error(request, 'Невозможно удалить книгу, пока '
                                    'существуют связанные с ней записи!')
            return render(request, 'books/delete.html', {'book': book},
                          status=409)
        book.delete()
        messages.success(request, 'Книга успешно удалена!')
        return redirect(reverse_lazy('books_list'))
