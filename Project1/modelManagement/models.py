from django.db import models

class Politic(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  carrec = models.CharField(max_length=255, null=True)
  partit = models.CharField(max_length=255, null=True)
  description = models.TextField(null=True)
#foto = models.ImageField(upload_to='images/',null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class PartitPolitic(models.Model):
  name = models.CharField(max_length=255)
  leader = models.CharField(max_length=255)
  ideology = models.CharField(max_length=255)
  members = models.CharField(max_length=255, null=True)
  description = models.TextField(null=True)


class Reunio(models.Model):
  subject = models.CharField(max_length=255, null=True)
  date = models.DateTimeField(null=True)
  ubication = models.CharField(max_length=255)
  members = models.CharField(max_length=255, null=True)
  description = models.TextField(null=True)
  #politic = models.ForeignKey(Politic, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.subject