# Generated by Django 5.1 on 2024-10-24 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0003_rename_created_at_watchlist_create_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='create_at',
            new_name='create',
        ),
    ]
