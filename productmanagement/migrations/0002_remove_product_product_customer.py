# Generated by Django 3.0.4 on 2020-07-10 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_Customer',
        ),
    ]
