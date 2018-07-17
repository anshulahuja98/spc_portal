from django.db import models


class ProgramAndBranch(models.Model):
    name = models.CharField(max_length=60)
    abbreviation = models.CharField(max_length=10)
    usable = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'branches'

    def __str__(self):
        return self.abbreviation


class Program(models.Model):
    name = models.CharField(max_length=60)
    abbreviation = models.CharField(max_length=10)
    usable = models.BooleanField(default=False)

    def __str__(self):
        return self.abbreviation
