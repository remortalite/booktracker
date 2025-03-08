from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import Book


class IndexPageView(View):
    def get(self, request):
        return HttpResponse('<h1>Hello, world!</h1>')


class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/list.html', {'books': books})
