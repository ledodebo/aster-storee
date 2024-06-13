# Generated by Django 4.2.7 on 2024-03-14 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_cartitem_cart_id'),
        ('accounts', '0008_rename_session_id_customer_device'),
    ]

    operations = [
        migrations.CreateModel(
            name='gust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('device', models.CharField(max_length=100)),
                ('catagofavry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
