# Generated by Django 4.2.9 on 2024-03-09 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]