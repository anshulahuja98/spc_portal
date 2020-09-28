from django.db import models
from django.contrib.auth.models import User
from student.models import ProgramAndBranch
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
import re


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
        ('5', 'Departmental Representative'),
        ('6', 'Team Member'),
        ('7', 'Web Development Team'),
        ('8', 'Internship Co-ordinator'),
        ('9', 'PG Representative'),
        ('10', 'Faculty Incharge'),
        ('11', 'Senior Assistant')
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

    def get_github_username(self):
        x = re.split("https://github.com/", str(self.github_link))
        return x[1]

    def get_linkedin_username(self):
        x = re.split("https://www.linkedin.com/in/", str(self.linkedin_link))
        return x[1]

    def __str__(self):
        return self.user.get_full_name()


class Volunteers(models.Model):
    YEAR_CHOICES = (
        ('1', 'UG Sophmore Year'),
        ('2', 'Postgraduation'),
        ('3', 'UG 3rd Year')
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


class HomeImageCarousel(models.Model):
    ordering = models.PositiveIntegerField(default=64)
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to='homepage-carousel', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class CareerCommittee(models.Model):
    DESIGNATION_CHOICES = (
        ('1', 'Chairman'),
        ('2', 'Convenor'),
        ('3', 'Members'),
        ('4', 'Faculty Incharge'),
    )
    name = models.CharField(max_length=64, blank=False, null=False, default='Member')
    email = models.EmailField(max_length=32, blank=False, null=False, default='member@gmail.com')
    designation = models.CharField(max_length=64, choices=DESIGNATION_CHOICES)
    department = models.TextField(max_length=64, default="Department")
    profile_image = models.ImageField(upload_to='contacts', blank=True, null=True)
    active = models.BooleanField(default=True)
    order_no = models.PositiveIntegerField(default=64)

    def __str__(self):
        return self.name


class NavBarSubOptions(models.Model):
    title = models.CharField(max_length=64)
    description = RichTextUploadingField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    use_custom_html = models.BooleanField(default=False)
    custom_html = models.CharField(max_length=64, blank=True, null=True)

    def clean(self):
        if self.use_custom_html and not self.custom_html:
            raise ValidationError('Custom HTML should be present with Use custom html option')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:navbarsuboptionpage', kwargs={'slug': self.slug})


class NavBarOptions(models.Model):
    title = models.CharField(max_length=64)
    sub_options = models.ManyToManyField(NavBarSubOptions)
    active = models.BooleanField(default=True)
    order_no = models.PositiveIntegerField(default=64)

    def __str__(self):
        return self.title


def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(event_pre_save_receiver, sender=NavBarSubOptions)
