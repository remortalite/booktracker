from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    author = models.CharField(max_length=255, verbose_name='Автор')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-name', '-author']

    def __str__(self):
        return self.author + ' — ' + self.name

    @property
    def full_name(self):
        return f'{self.author} — {self.name}'
