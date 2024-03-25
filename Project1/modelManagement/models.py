from django.db import models

class Politic(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  carrec = models.CharField(max_length=255, null=True)
  partit = models.CharField(max_length=255, null=True)
  description = models.TextField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class PartitPolitic(models.Model):
  name = models.CharField(max_length=255)
  leader = models.CharField(max_length=255)
  ideology = models.CharField(max_length=255)
  description = models.TextField()

class Reunio(models.Model):
  date = models.DateField()
  hours = models.IntegerField()
  ubication = models.CharField(max_length=255)