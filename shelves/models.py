from django.db import models
from django.contrib.auth.models import User

from books.models import Book


class Shelf(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             on_delete=models.PROTECT)
    books = models.ManyToManyField(Book,
                                   related_name='books',
                                   verbose_name='Книги')

    class Meta:
        verbose_name = 'Полка'
        verbose_name_plural = 'Полки'

    def __str__(self):
        return f"{self.name} ({self.user.username})"
