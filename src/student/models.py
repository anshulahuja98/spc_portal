from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=60)
    usable = models.BooleanField(default=False)


class Program(models.Model):
    name = models.CharField(max_length=60)
    usable = models.BooleanField(default=False)
