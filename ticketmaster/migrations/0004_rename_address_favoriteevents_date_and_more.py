# Generated by Django 4.2.7 on 2023-11-30 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketmaster', '0003_favoriteevents_delete_favoritedevents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoriteevents',
            old_name='address',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='favoriteevents',
            name='session_id',
        ),
        migrations.AddField(
            model_name='favoriteevents',
            name='venueAddress',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favoriteevents',
            name='venueCity',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favoriteevents',
            name='venueState',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
