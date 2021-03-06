# Generated by Django 3.2.6 on 2021-08-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',), 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique=True, verbose_name='Url'),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique=True, verbose_name='Url'),
        ),
    ]
