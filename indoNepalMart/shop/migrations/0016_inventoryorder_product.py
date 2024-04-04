# Generated by Django 5.0.2 on 2024-03-01 07:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_rename_sno_inventoryorder_order_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryorder',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]