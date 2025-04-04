# Generated by Django 5.1.7 on 2025-03-08 03:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='record',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='record',
            name='status',
            field=models.CharField(choices=[('on_hold', 'Отложено'), ('reading', 'Читаю'), ('finished', 'Закончено'), ('to_read', 'Прочитать')], default='to_read', max_length=16, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='record',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Изменено'),
        ),
    ]
