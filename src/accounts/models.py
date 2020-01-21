from django.db import models
from django.contrib.auth.models import User
from student.models import ProgramAndBranch
from django.db.models.signals import pre_save, post_delete
import random
from django.core.mail import get_connection, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.apps import apps


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
    ug_gpa = models.FloatField(null=True, blank=True)
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
    std_image = models.ImageField(default='default.jpg', upload_to='student_images')
    registration_timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def student_register_email(self):
        from_email = settings.SPC_EMAIL
        with get_connection(
                username=from_email,
                password=settings.SPC_EMAIL_PASSWORD
        ) as connection:
            subject = "Registered with SPC"
            to_email = [self.user.email, ]
            html_content = render_to_string("accounts/student_register_email.html",
                                            {'username': self.user.username, 'email': self.user.email})
            text_content = strip_tags(html_content)
            message = EmailMultiAlternatives(subject=subject, body=text_content, from_email=from_email, to=to_email,
                                             connection=connection)
            message.attach_alternative(html_content, "text/html")
            message.send()

    def __str__(self):
        return self.user.get_full_name()

    # Used in csv export to get list of all applied offers in string
    def get_all_applied_offers_str(self):
        offers = apps.get_model('company.InternshipAdvertisement').objects.filter(
            id__in=apps.get_model('company.InternshipOffer').objects.filter(student__user=self.user).values_list(
                'profile'))

        offers.union(apps.get_model('company.JobAdvertisement').objects.filter(
            id__in=apps.get_model('company.JobOffer').objects.filter(
                student__user=self.user).values_list(
                'profile')))

        offer_list = ''
        for i in range(offers.count()):
            offer_list += str(offers[i]) + ', '
        return offer_list


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
    contact = models.CharField(max_length=20)
    registration_timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def company_register_email(self):
        from_email = settings.SPC_EMAIL
        with get_connection(
                username=from_email,
                password=settings.SPC_EMAIL_PASSWORD
        ) as connection:
            subject = "Registered with SPC"
            to_email = [self.user.username, ]
            html_content = render_to_string("accounts/company_register_email.html", {'username': self.user.username})
            text_content = strip_tags(html_content)
            message = EmailMultiAlternatives(subject=subject, body=text_content, from_email=from_email, to=to_email,
                                             connection=connection)
            message.attach_alternative(html_content, "text/html")
            message.send()

    def company_details_email(self):
        from_email = settings.SPC_EMAIL
        with get_connection(
                username=from_email,
                password=settings.SPC_EMAIL_PASSWORD
        ) as connection:
            subject = "Company Registered with SPC"
            to_email = settings.RECIPIENT_EMAILS
            html_content = render_to_string("accounts/company_details_email.html",
                                            {'name': self.name, 'email': self.user.username,
                                             'domain': self.domain, 'url': self.url,
                                             'city': self.city, 'state': self.state,
                                             'contact': self.contact})
            text_content = strip_tags(html_content)
            message = EmailMultiAlternatives(subject=subject, body=text_content, from_email=from_email, to=to_email,
                                             connection=connection)
            message.attach_alternative(html_content, "text/html")
            message.send()


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


def event_pre_save_receiver_student(sender, instance, *args, **kwargs):
    if not instance.roll_no:
        instance.roll_no = instance.user.username


pre_save.connect(event_pre_save_receiver_student, sender=StudentProfile)


def event_pre_save_receiver_resume(sender, instance, *args, **kwargs):
    if instance.student.user.first_name not in instance.file.name or \
            instance.student.user.last_name not in instance.file.name or \
            instance.student.user.username not in instance.file.name or \
            'IITJodhpur.pdf' not in instance.file.name \
            and instance._state.adding is True:
        instance.file.name = instance.student.user.first_name + '_' + instance.student.user.last_name \
                             + '_' + instance.student.user.username + '_' + str(random.randint(1, 10001)) + \
                             '_' + 'IITJodhpur.pdf'
    if not instance.reference:
        instance.reference = instance.file.name


pre_save.connect(event_pre_save_receiver_resume, sender=Resume)


def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()


post_delete.connect(delete_user, sender=StudentProfile)
post_delete.connect(delete_user, sender=CompanyProfile)
