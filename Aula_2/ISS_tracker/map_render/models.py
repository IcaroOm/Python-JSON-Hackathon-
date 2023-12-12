from django.db import models


class IssLocation(models.Model):
    timestamp = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - ({self.latitude}, {self.longitude})"
