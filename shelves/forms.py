from django.forms import ModelForm

from .models import Shelf


class ShelfForm(ModelForm):
    class Meta:
        model = Shelf
        fields = '__all__'
