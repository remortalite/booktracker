from django import forms


class BookForm(forms.Form):
    name = forms.CharField(max_length=255, label='Название')
    author = forms.CharField(max_length=255, label='Автор')
