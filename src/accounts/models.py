from django.db import models
from django.contrib.auth.models import User
from student.models import ProgramAndBranch
from django.db.models.signals import pre_save
import random


class StudentProfile(models.Model):
    # Choices
    CATEGORY = (
        ('1', 'General'),
        ('2', 'OBC'),
        ('3', 'SC'),
        ('4', 'ST'),
    )
    NATION = (
        ('1', 'Indian'),
        ('2', 'Other'),
    )
    # Validators

    # Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=11)
    year = models.SmallIntegerField()
    program_branch = models.ForeignKey(ProgramAndBranch, on_delete=models.SET_NULL, null=True)
    # program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    gpa = models.FloatField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORY)
    jee_air = models.IntegerField(null=True, blank=True)
    physical_disability = models.BooleanField(default=False)
    nationality = models.CharField(max_length=10, choices=NATION)
    permanent_address = models.TextField()
    current_address = models.TextField()
    x_year = models.SmallIntegerField()
    x_board_name = models.CharField(max_length=100)
    x_percentage = models.CharField(max_length=10)
    xii_year = models.SmallIntegerField()
    xii_board_name = models.CharField(max_length=100)
    xii_percentage = models.CharField(max_length=10)
    banned = models.BooleanField(default=False)
    placed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()


class CompanyProfile(models.Model):
    # Choices
    NATION = (
        ('1', 'Indian'),
        ('2', 'Other'),
    )
    # Model
    name = models.CharField(max_length=50, help_text="Name of the company")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    domain = models.CharField(max_length=30, help_text="Type of company like banking/consulting etc ")  # add choices
    url = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=15, null=True, blank=True)
    state = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=15, choices=NATION)
    pin_code = models.CharField(max_length=10, blank=True, null=True)
    job_offers = models.ManyToManyField(StudentProfile, through='company.JobOffer',
                                        through_fields=('company', 'student'), related_name='joboffers')
    internship_offers = models.ManyToManyField(StudentProfile, through='company.InternshipOffer',
                                               through_fields=('company', 'student'), related_name='internshipoffers')

    def __str__(self):
        return self.name


class CompanyPerson(models.Model):
    name = models.CharField(max_length=30)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, help_text="For phone numbers outside India, please add country code")
    email = models.EmailField()


class Resume(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resume')
    is_verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=200, null=True, blank=True,
                                 help_text="Enter a reference name for this resume by which you can remember the details of this particular resume")

    def __str__(self):
        if not self.reference:
            return "No reference"
        else:
            return self.reference


def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.roll_no:
        instance.roll_no = instance.user.username


pre_save.connect(event_pre_save_receiver, sender=StudentProfile)


def event_pre_save_receiver_resume(sender, instance, *args, **kwargs):
    if instance.student.user.first_name not in instance.file.name or instance.student.user.last_name not in instance.file.name or instance.student.user.username not in instance.file.name or 'IITJodhpur.pdf' not in instance.file.name:
        instance.file.name = instance.student.user.first_name + '_' + instance.student.user.last_name + '_' + instance.student.user.username + '_' + str(
            random.randint(
                1, 10001)) + '_' + 'IITJodhpur.pdf'


pre_save.connect(event_pre_save_receiver_resume, sender=Resume)
