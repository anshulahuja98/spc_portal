from django.db import models


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
    designation = models.CharField(max_length=64 , null=True)
    testimonial = models.TextField(null=False)
    alumni_image = models.ImageField(upload_to='testimonial')
    active = models.BooleanField(default=True)
    ranking = models.PositiveSmallIntegerField(default=512)

    def __str__(self):
        return self.alumni_name
