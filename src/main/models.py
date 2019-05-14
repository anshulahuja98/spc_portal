from django.db import models


class HomeImageCarousel(models.Model):
    ordering = models.PositiveIntegerField(default=64)
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to='homepage-carousel', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
