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


class Record(models.Model):
    class Status(models.TextChoices):
        ON_HOLD = 'on_hold', 'Отложено'
        READING = 'reading', 'Читаю'
        FINISHED = 'finished', 'Закончено'
        TO_READ = 'to_read', 'Прочитать'
    book = models.ForeignKey(Book, on_delete=models.PROTECT,
                             verbose_name='Книга')
    status = models.CharField(max_length=16,
                              choices=Status.choices,
                              default=Status.TO_READ,
                              verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Изменено')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
