from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse

from .models import Book
from .forms import BookForm


class IndexPageView(View):
    def get(self, request):
        return HttpResponse('<h1>Hello, world!</h1>')


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/list.html', {'books': books})


class BookDetailView(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        return render(request, 'books/detail.html', {'book': book})


class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'books/create.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book()
            book.author = form.cleaned_data['author']
            book.name = form.cleaned_data['name']
            book.save()
            return redirect(reverse_lazy('books_list'))
        return render(request, 'books/create.html', {'form': form})


class BookUpdateView(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        form = BookForm(initial=book)
        return render(request, 'books/update.html', {'form': form})

    def post(self, request):
        pass
