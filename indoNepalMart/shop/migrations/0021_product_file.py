# Generated by Django 5.0.2 on 2024-03-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='shop/our_product_images'),
        ),
    ]
