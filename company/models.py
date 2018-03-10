from django.db import models
from accounts import models as account_models

class JobOffer(models.Model):
    company = models.ForeignKey(account_models.CompanyProfile, on_delete=models.CASCADE, related_name='joboffer',blank=True)
    #job prof
    jobdesig=models.CharField(max_length=30)
    jobdescrip=models.CharField(max_length=50)
    tentativejoindate=models.DateField
    tentativejobloc=models.CharField(max_length=50)
    ads=models.FileField(upload_to='ads')
    #package details
    ctc=models.IntegerField
    grossSal=models.IntegerField
    bonus=models.IntegerField(blank=True)
    bond=models.BooleanField
    #selection process
    resume=models.BooleanField
    aptTest = models.BooleanField
    techTest = models.BooleanField
    gd = models.BooleanField
    techInterview= models.BooleanField
    hr = models.BooleanField
    medical  = models.BooleanField
    minGPA = models.FloatField
    #logistic
    numberMembers=models.IntegerField
    otherDetails=models.TextField

class InternOffer(models.Model):
    company=models.ForeignKey(account_models.CompanyProfile,on_delete=models.CASCADE,related_name='internoffer',blank=True,null=True)
    # job prof
    jobdesig = models.CharField(max_length=30)
    jobdescrip = models.CharField(max_length=50)
    tentativejoindate = models.DateField
    tentativejobloc = models.CharField(max_length=50)
    ads = models.FileField(upload_to='ads')
    # package details
    ctc = models.IntegerField
    grossSal = models.IntegerField
    bonus = models.IntegerField(blank=True)
    bond = models.BooleanField
    # selection process
    resume = models.BooleanField
    aptTest = models.BooleanField
    techTest = models.BooleanField
    gd = models.BooleanField
    techInterview = models.BooleanField
    hr = models.BooleanField
    medical = models.BooleanField
    minGPA = models.FloatField
    # logistic
    numberMembers = models.IntegerField
    otherDetails = models.TextField



class Program(models.Model):
    name=models.CharField(max_length=30)
    branch = models.CharField(max_length=64)
    usable=models.BooleanField(default=False)
