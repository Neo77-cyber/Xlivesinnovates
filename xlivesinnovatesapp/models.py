from django.db import models
from django.utils import timezone

class FishPond(models.Model):
    WATER_LEVEL_CHOICES = [
        ('25%', '25%'),
        ('50%', '50%'),
        ('75%', '75%'),
        ('100%', '100%'),
    ]

    WATER_QUALITY_CHOICES = [
        ('clear', 'Clear'),
        ('fairly_clear', 'Fairly Clear'),
        ('cloudy', 'Cloudy'),
    ]

    ALGAE_PRESENCE_CHOICES = [
        ('none', 'None'),
        ('low', 'Low'),
        ('high', 'High'),
    ]

    FEED_TYPE_CHOICES = [
        ('2mm', '2mm'),
        ('3mm', '3mm'),
        ('4mm', '4mm'),
        ('6mm', '6mm'),
        ('9mm', '9mm'),
    ]

    water_change_date = models.DateField(default=timezone.now)
    water_change_time = models.TimeField()
    water_level = models.CharField(max_length=10, choices=WATER_LEVEL_CHOICES, blank=False)
    water_quality = models.CharField(max_length=20, choices=WATER_QUALITY_CHOICES, blank=False)
    algae_presence = models.CharField(max_length=10, choices=ALGAE_PRESENCE_CHOICES, blank=False)
    feed_type = models.CharField(max_length=10, choices=FEED_TYPE_CHOICES, blank=False)
    feed_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    feed_time = models.TimeField()
    number_of_fish_stocked = models.IntegerField()
    fish_size_or_weight = models.CharField(max_length=50)
    signs_of_illness = models.TextField(blank=True)
    medications_administered = models.TextField(blank=True)
    number_of_fish_harvested = models.IntegerField()
    harvested_fish_size_or_weight = models.CharField(max_length=50)
    general_observations = models.TextField(blank=True)
    unexpected_events = models.TextField(blank=True)
    fuel_cost = models.DecimalField(max_digits=10, decimal_places=2)
    repairs_cost = models.DecimalField(max_digits=10, decimal_places=2)
