# Generated by Django 4.2.7 on 2023-11-15 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customer_catagofavry_product_ava'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
