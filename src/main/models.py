from django.db import models
from django.contrib.auth.models import User
from student.models import ProgramAndBranch


class News(models.Model):
    title = models.CharField(max_length=64, blank=True)
    order_no = models.PositiveSmallIntegerField(default=512)
    content = models.TextField(max_length=512)
    active = models.BooleanField(default=True)
    document = models.FileField(upload_to='news', blank=True, null=True)
    file_title = models.CharField(max_length=64, default='Read More')
    link = models.URLField(blank=True, null=True)
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


class CoreTeamContacts(models.Model):
    DESIGNATION_CHOICES = (
        ('1', 'Chairman'),
        ('2', 'Placement Officer'),
        ('3', 'Project Superintendent'),
        ('4', 'Student Co-ordinator'),
        ('5', 'Department Representative'),
        ('6', 'Team Member'),
        ('7', 'Web Development Team'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=64, choices=DESIGNATION_CHOICES)
    sub_designation = models.CharField(max_length=64, default='Office of Student Placement')
    program_branch = models.ForeignKey(ProgramAndBranch, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='contacts', blank=True, null=True)
    active = models.BooleanField(default=True)
    order_no = models.PositiveIntegerField(default=64)

    def __str__(self):
        return self.user.get_full_name()


class Volunteers(models.Model):
    YEAR_CHOICES = (
        ('1', 'Sophmore Year'),
        ('2', 'Postgraduation'),
    )

    name = models.CharField(max_length=64)
    year = models.CharField(max_length=64, choices=YEAR_CHOICES, null=True)
    program_branch = models.ForeignKey(ProgramAndBranch, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)
    order_no = models.PositiveIntegerField(default=64)

    def __str__(self):
        return self.name
      

 class AlumniTestimonial(models.Model):
    alumni_name = models.CharField(max_length=64)
    company_working = models.CharField(max_length=64)
    designation = models.CharField(max_length=64, null=True)
    testimonial = models.TextField(null=False)
    alumni_image = models.ImageField(upload_to='alumni-testimonial')
    active = models.BooleanField(default=True)
    ranking = models.PositiveSmallIntegerField(default=512)

    def __str__(self):
        return self.alumni_name

