# Generated by Django 4.2.7 on 2024-05-15 18:04

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0060_delete_test_alter_product_genders'),
    ]

    operations = [
      
        migrations.AlterField(
            model_name='product',
            name='genders',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female'), ('u', 'unisex')], max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=None, size=[500, 300], upload_to='uploads/product'),
        ),
    ]
