# Generated by Django 5.0.2 on 2024-03-08 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_product_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='file',
        ),
    ]
