# Generated by Django 5.0.3 on 2024-05-13 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moobile', '0008_product_image_delete_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
    ]
