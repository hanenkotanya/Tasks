# Generated by Django 5.0.2 on 2024-02-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_restaurant_mini_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='mini_image',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='mini_media'),
        ),
    ]
