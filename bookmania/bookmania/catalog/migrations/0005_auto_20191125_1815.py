# Generated by Django 2.2.6 on 2019-11-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_book_bpdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='first_name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='first_name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='summary_en',
            field=models.TextField(help_text='Enter a brief description of the book', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='summary_ru',
            field=models.TextField(help_text='Enter a brief description of the book', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
    ]