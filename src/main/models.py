from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50, blank=True)
    order_no = models.PositiveSmallIntegerField(default=500)
    content = models.TextField(max_length=250)
    active = models.BooleanField()
    document = models.FileField(upload_to='news', blank=True, null=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
