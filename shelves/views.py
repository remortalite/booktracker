from django.shortcuts import (render, redirect,
                              get_list_or_404, get_object_or_404)
from django.urls import reverse_lazy

from .forms import ShelfForm
from .models import Shelf


def shelf_list_view(request):
    if request.method == 'GET':
        shelves = get_list_or_404(Shelf)
        return render(request, 'shelves/list.html', {'shelves': shelves})


def shelf_detail_view(request, shelf_id):
    if request.method == 'GET':
        shelf = get_object_or_404(Shelf, id=shelf_id)
        return render(request, 'shelves/detail.html', {'shelf': shelf})


def shelf_create_view(request):
    if request.method == 'GET':
        form = ShelfForm()
        return render(request, 'shelves/form.html', {'form': form})
    elif request.method == 'POST':
        form = ShelfForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('shelf_list'))
        return render(request, 'shelves/form.html', {'form': form})
