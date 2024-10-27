# seasense_backend/models.py

from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, related_name='states', on_delete=models.CASCADE)
    beaches = models.TextField(blank=True, null=True)  # New field to store beaches as text

    def __str__(self):
        return self.name
