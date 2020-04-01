# Generated by Django 3.0.4 on 2020-04-01 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(default='none', max_length=100)),
                ('continet_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=26, null=True)),
                ('state', models.CharField(max_length=26, null=True)),
                ('zip', models.CharField(max_length=6, null=True)),
                ('notes', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=26, null=True)),
                ('city', models.CharField(max_length=26, null=True)),
                ('state', models.CharField(max_length=26, null=True)),
                ('zip', models.CharField(max_length=6, null=True)),
                ('notes', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(default='none', max_length=100)),
                ('supplier_created', models.DateTimeField(auto_now_add=True)),
                ('supplier_country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productmanagement.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='none', max_length=50)),
                ('product_manufacturer', models.CharField(default='none', max_length=50)),
                ('product_price', models.IntegerField(default=10)),
                ('product_available_status', models.BooleanField(default=True)),
                ('product_Supplier', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='productmanagement.supplier')),
            ],
        ),
    ]
