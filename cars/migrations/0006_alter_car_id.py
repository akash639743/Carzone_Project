# Generated by Django 3.2.5 on 2021-08-13 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_rename_transmissionf_car_transmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]