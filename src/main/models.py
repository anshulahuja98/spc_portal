from django.db import models


class HomeImageCarousel(models.Model):
    image_no = models.PositiveIntegerField(default=64)
    image_title = models.CharField(default="image", max_length=64)
    image_carousel = models.ImageField(upload_to='', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.image_title
