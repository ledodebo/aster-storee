# Generated by Django 4.2.7 on 2024-01-29 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_cartitem_id_cartitem_cart_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart_id',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
