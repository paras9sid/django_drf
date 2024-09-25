# Generated by Django 5.1 on 2024-09-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_of_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
