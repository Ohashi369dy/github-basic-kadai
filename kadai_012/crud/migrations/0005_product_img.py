# Generated by Django 4.1.7 on 2025-06-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_rename_cayegory_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='noImage.png', upload_to=''),
        ),
    ]
