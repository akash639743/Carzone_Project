# Generated by Django 3.2.5 on 2021-08-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_rename_ftwitter_link_team_twitter_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]