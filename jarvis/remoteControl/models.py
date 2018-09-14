from django.db import models
from django.utils import timezone

# Create your models here.

class Machine(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  registered = models.DateTimeField(default=timezone.now)
  location = models.CharField(max_length=200, blank=True, default='')
  notes = models.TextField()
  mac = models.CharField(max_length=50)
  ip = models.CharField(max_length=50)
  lastConnected = models.DateTimeField(default=timezone.now, blank=True)

  def refreshLastConnected(self):
    self.lastConnected = timezone.now()
    self.save()

  def __str__(self):
        return self.name

class Order(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  command = models.CharField(max_length=100)
  machineId = models.ForeignKey('Machine', on_delete=models.CASCADE)
  createdAt = models.DateTimeField(default=timezone.now, blank=True)
  executed = models.BooleanField()

  def __str__(self):
        return self.command
# class User(models.Model):
