from django.db import models

# Create your models here.

class Buyer(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=200, null=True, blank=True)
