# Generated by Django 5.0.2 on 2024-02-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_restaurant_mini_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='image',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='Документ с меню'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Первая страница меню'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Вторая страница меню'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Третяя страница меню'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='mini_image',
            field=models.ImageField(blank=True, default='media_mini/default.jpg', null=True, upload_to='media_mini'),
        ),
    ]