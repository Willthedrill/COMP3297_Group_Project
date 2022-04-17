from importlib.util import module_for_loader
from django.db import models
from matplotlib.backend_bases import LocationEvent

# Create your models here.
class MemberRecord(models.Model):
    uid = models.CharField(max_length = 10)
    name = models.CharField(max_length = 150)

class Record(models.Model):
    member = models.ForeignKey(
        MemberRecord, on_delete=models.CASCADE)
    venue = models.ForeignKey(
        VenueRecord, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    type = models.CharField(max_length = 10)

class VenueRecord(models.Model):
    venue_code=models.CharField(max_length=20)
    location=models.CharField(max_length=150)
    type=models.CharField(max_length=2)
    capacity=models.IntegerField()
