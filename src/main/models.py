from django.db import models


class PastRecruiters(models.Model):
    company_order_no = models.PositiveIntegerField(default=64)
    company_name = models.CharField(max_length=64)
    company_logo = models.ImageField(upload_to='company-logo', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name

class Testimonial(models.Model):
    student_name = models.CharField(max_length=64)
    company_working = models.CharField(max_length=64)
    post_working = models.CharField(max_length=64)
    alumni_word = models.TextField(null=True)
    student_image = models.ImageField(upload_to='testimonial', null=False)
    active = models.BooleanField(default=False)
    ranking = models.PositiveSmallIntegerField(default=512)

    def __str__(self):
        return self.student_name
