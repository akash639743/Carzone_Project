# Generated by Django 3.2.5 on 2021-07-30 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_features'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='transmissionf',
            new_name='transmission',
        ),
    ]
