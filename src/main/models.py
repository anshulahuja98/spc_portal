from django.db import models


class PastRecruiters(models.Model):
    company_order_no = models.PositiveIntegerField(default=64)
    company_name = models.CharField(max_length=64)
    company_logo = models.ImageField(upload_to='company-logo', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name


class Contacts(models.Model):
    DESIGNATION_CHOICES = (
        ('Chairman', 'Chairman'),
        ('Placement Officer', 'Placement Officer'),
        ('Project Superintendent', 'Project Superintendent'),
        ('Student Co-ordinator', 'Student Co-ordinator'),
        ('Departmental Student Representative', 'Departmental Student Representative'),
        ('Team Member', 'Team Member'),
        ('Web Development Team', 'Web Development Team'),
        ('Volunteer-Sophomore Year', 'Volunteer-Sophomore Year'),
        ('Volunteer-Postgraduation', 'Volunteer-Postgraduation'),
    )

    name = models.CharField(max_length=64, blank=False, null=False)
    designation = models.CharField(max_length=64, choices=DESIGNATION_CHOICES, default='Volunteer-Sophomore Year')
    sub_designation = models.CharField(max_length=64, default='Office of Student Placement')
    branch = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(max_length=64, blank=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    profile_image = models.ImageField(upload_to='contacts', blank=True, null=True)
    active = models.BooleanField(default=True)
    order_no = models.PositiveIntegerField(default=64)
