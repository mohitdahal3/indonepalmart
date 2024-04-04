# Generated by Django 5.0.2 on 2024-02-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='secondary_phone_number',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_picture2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='shop/images'),
        ),
    ]