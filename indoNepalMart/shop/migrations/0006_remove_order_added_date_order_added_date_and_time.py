# Generated by Django 5.0.2 on 2024-02-27 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_order_product_picture1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='added_date',
        ),
        migrations.AddField(
            model_name='order',
            name='added_date_and_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
