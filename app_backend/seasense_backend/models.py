# seasense_backend/models.py

from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Ensure name is unique for clarity

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, related_name='states', on_delete=models.CASCADE)
    beaches = models.TextField(blank=True, null=True)  # Stores a comma-separated list of beaches

    def __str__(self):
        return f"{self.name} in {self.region.name}"
