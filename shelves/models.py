from django.db import models
from django.contrib.auth.models import User

from books.models import Book


class Shelf(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    book = models.ManyToManyField(Book,
                                  related_name='books',
                                  verbose_name='Книги')
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             on_delete=models.PROTECT)
