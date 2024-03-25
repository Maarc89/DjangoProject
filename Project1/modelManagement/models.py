from django.db import models

class Person(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"