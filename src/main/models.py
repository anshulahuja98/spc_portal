from django.db import models


class News(models.Model):
    title = models.CharField(max_length=64, blank=True)
    order_no = models.PositiveSmallIntegerField(default=512)
    content = models.TextField(max_length=512)
    active = models.BooleanField()
    document = models.FileField(upload_to='news', blank=True, null=True)
    file_title = models.CharField(max_length=64, default='Read More')
    link = models.URLField(blank=True)
    link_title = models.CharField(max_length=64, default='Link')

    def __str__(self):
        return self.title


class PastRecruiters(models.Model):
    company_order_no = models.PositiveIntegerField(default=64)
    company_name = models.CharField(max_length=64)
    company_logo = models.ImageField(upload_to='company-logo', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name


class AlumniTestimonial(models.Model):
    alumni_name = models.CharField(max_length=64)
    company_working = models.CharField(max_length=64)
    designation = models.CharField(max_length=64, null=True)
    testimonial = models.TextField(null=False)
    alumni_image = models.ImageField(upload_to='testimonial')
    active = models.BooleanField(default=True)
    ranking = models.PositiveSmallIntegerField(default=512)

    def __str__(self):
        return self.alumni_name
