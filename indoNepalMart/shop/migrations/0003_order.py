# Generated by Django 5.0.2 on 2024-02-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_contact_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_number', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(default='', max_length=100)),
                ('customer_phone_number', models.CharField(default='', max_length=20)),
                ('customer_email', models.CharField(default='', max_length=200)),
                ('customer_address', models.CharField(default='', max_length=200)),
                ('product_picture1', models.ImageField(default='', upload_to='shop/images')),
                ('product_picture2', models.ImageField(default='', upload_to='shop/images')),
                ('product_link', models.CharField(default='', max_length=500)),
                ('added_date', models.DateField(auto_now=True)),
            ],
        ),
    ]