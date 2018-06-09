from django.db import models
from accounts.models import CompanyProfile


class JobOffer(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='joboffer',
                                blank=True)
    # job prof
    job_designation = models.CharField(max_length=30)
    job_description = models.CharField(max_length=50)
    tentative_join_date = models.DateField()
    tentative_job_loc = models.CharField(max_length=50)
    ads = models.FileField(upload_to='ads')
    # package details
    ctc = models.IntegerField
    gross_sal = models.IntegerField
    bonus = models.IntegerField(blank=True)
    bond = models.BooleanField
    # selection process
    resume = models.BooleanField
    aptitude_test = models.BooleanField
    technical_test = models.BooleanField
    group_discussion = models.BooleanField
    technical_interview = models.BooleanField
    hr = models.BooleanField
    medical = models.BooleanField
    min_gpa = models.FloatField
    # logistic
    number_members = models.IntegerField
    other_details = models.TextField


class InternOffer(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='joboffer',
                                blank=True)
    # job prof
    job_designation = models.CharField(max_length=30)
    job_description = models.CharField(max_length=50)
    tentative_join_date = models.DateField()
    tentative_job_loc = models.CharField(max_length=50)
    ads = models.FileField(upload_to='ads')
    # package details
    ctc = models.IntegerField
    gross_sal = models.IntegerField
    bonus = models.IntegerField(blank=True)
    bond = models.BooleanField
    # selection process
    resume = models.BooleanField
    aptitude_test = models.BooleanField
    technical_test = models.BooleanField
    group_discussion = models.BooleanField
    technical_interview = models.BooleanField
    hr = models.BooleanField
    medical = models.BooleanField
    min_gpa = models.FloatField
    # logistic
    number_members = models.IntegerField
    other_details = models.TextField


class Program(models.Model):
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=64)
    usable = models.BooleanField(default=False)
