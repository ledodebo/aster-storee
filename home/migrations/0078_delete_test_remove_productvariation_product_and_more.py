# Generated by Django 4.2.7 on 2024-06-08 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0077_delete_test_productvariation_ava'),
    ]

    operations = [
       
        migrations.RemoveField(
            model_name='productvariation',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='ProductVariation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='home.productvariation'),
            preserve_default=False,
        ),
    ]
