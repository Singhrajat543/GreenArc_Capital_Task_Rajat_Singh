# Generated by Django 3.2.4 on 2021-07-09 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdplace',
            name='product_image',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to='productimg'),
        ),
    ]