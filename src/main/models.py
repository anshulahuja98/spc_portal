from django.db import models
from django.shortcuts import render

class nEws(models.Model):
    order_no = models.PositiveIntegerField()
    content = models.TextField(max_length=100)
    do_show = models.BooleanField()
    document = models.FileField(upload_to='./staticfiles',blank = True)

    def __str__(self):
        return self.content