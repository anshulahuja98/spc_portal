from django.db import models
from accounts.models import CompanyProfile


class JobAdvertisement(models.Model):
    # job prof
    designation = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    tentative_join_date = models.DateField()
    tentative_job_location = models.CharField(max_length=50)
    ads = models.FileField(upload_to='ads')
    # package details
    ctc = models.IntegerField()
    gross_salary = models.PositiveIntegerField()
    bonus = models.PositiveIntegerField(blank=True, default=0)
    bond = models.BooleanField()
    # selection process
    resume_required = models.BooleanField()
    aptitude_test_required = models.BooleanField()
    technical_test_required = models.BooleanField()
    group_discussion_required = models.BooleanField()
    technical_interview_required = models.BooleanField()
    hr_round_required = models.BooleanField()
    medical_test_required = models.BooleanField()
    min_gpa = models.FloatField()
    # logistic
    number_of_members = models.PositiveIntegerField()
    other_details = models.TextField()


class InternAdvertisement(models.Model):
    # company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='internoffer',
    #                             blank=True)
    # job prof
    designation = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    tentative_join_date = models.DateField()
    tentative_job_location = models.CharField(max_length=50)
    ads = models.FileField(upload_to='ads')
    # package details
    ctc = models.IntegerField()
    gross_salary = models.PositiveIntegerField()
    bonus = models.PositiveIntegerField(blank=True, default=0)
    bond = models.BooleanField()
    # selection process
    resume_required = models.BooleanField()
    aptitude_test_required = models.BooleanField()
    technical_test_required = models.BooleanField()
    group_discussion_required = models.BooleanField()
    technical_interview_required = models.BooleanField()
    hr_round_required = models.BooleanField()
    medical_test_required = models.BooleanField()
    min_gpa = models.FloatField()
    # logistic
    number_of_members = models.PositiveIntegerField()
    other_details = models.TextField()


class Program(models.Model):
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=64)
    usable = models.BooleanField(default=False)
