# Generated by Django 4.2.9 on 2024-04-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_details_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Clothes', 'CLOTHES'), ('SHOES', 'Shoes')], max_length=100),
        ),
    ]
