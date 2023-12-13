from django.db import models


class FavoriteEvents(models.Model):
    is_going = models.BooleanField(default=False)
    is_favorited = models.BooleanField(default=False)
    entry_model_id = models.CharField(max_length=60)
    event = models.CharField(max_length=60)
    venue = models.CharField(max_length=60)
    venueCity = models.CharField(max_length=60)
    venueState = models.CharField(max_length=60)
    venueAddress = models.CharField(max_length=60)
    date = models.CharField(max_length=60)
    time = models.CharField(max_length=60)
    link = models.CharField(max_length=60)
    thumbnailURL = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.event} at {self.venue}, {self.venueCity}, {self.venueState} on {self.date}"
