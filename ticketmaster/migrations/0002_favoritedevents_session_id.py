# Generated by Django 4.2.7 on 2023-11-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketmaster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritedevents',
            name='session_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
