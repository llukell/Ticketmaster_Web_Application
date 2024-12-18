# Generated by Django 4.2.7 on 2023-12-08 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketmaster', '0006_alter_favoriteevents_eventid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoriteevents',
            old_name='eventId',
            new_name='entry_model_id',
        ),
        migrations.AddField(
            model_name='favoriteevents',
            name='event_model_id',
            field=models.CharField(default=None, max_length=60),
            preserve_default=False,
        ),
    ]
