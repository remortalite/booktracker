from django import forms

from .models import Book
from shelves.models import Shelf


class BookForm(forms.ModelForm):

    shelf = forms.ModelChoiceField(queryset=Shelf.objects.all(), label='Полка')

    class Meta:
        model = Book
        fields = ('name', 'author',)
