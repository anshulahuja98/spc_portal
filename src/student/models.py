from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=60)
    usable = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'branches'

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=60)
    usable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
