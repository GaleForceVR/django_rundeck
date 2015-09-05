from django.db import models
from django.contrib.auth.models import User
import datetime
# from django.utils.datetime import date
from django.utils.timezone import timedelta

# Create your models here.
class Route(models.Model):
  distance = models.DecimalField(max_digits=5,decimal_places=2)
  location = models.CharField(max_length=60)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # created_at = models.DateTimeField(default=datetime.datetime.now)
  # updated_at = models.DateTimeField(default=datetime.datetime.now)

  def __str__(self):
    return self.location + ": " + self.distance.__str__() + " mi"


class Effort(models.Model):
  user = models.ForeignKey(User)
  route = models.ForeignKey(Route)
  total_time = models.DurationField()
  total_distance = models.DecimalField(max_digits=5,decimal_places=2)
  effort_time = models.DateTimeField(default=datetime.datetime.now)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.route.location + ": " + self.route.distance.__str__() + "mi: " + self.total_time.__str__()

class Split(models.Model):
  effort = models.ForeignKey(Effort)
  distance = models.DecimalField(max_digits=5,decimal_places=2)
  split_time = models.DurationField()

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # def custom_format(td):
  #   minutes

    # def custom_format(td):
    #     seconds, microseconds = divmod(td.microseconds, 100)
    #     minutes, seconds = divmod(td.seconds, 60)
    #     hours, minutes = divmod(minutes, 60)
    #     return '{:d}:{:02d}:{:02d}.{:02d}'.format(hours, minutes, seconds, microseconds)

  def __str__(self):
    return "SPLIT: " + self.split_time.__str__().strip('0') + " -- " + self.distance.__str__() + "mi"
