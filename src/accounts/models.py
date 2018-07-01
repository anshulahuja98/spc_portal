from django.db import models
from django.contrib.auth.models import User
from student.models import Branch, Program


class StudentProfile(models.Model):
    # Choices
    CATEGORY = (
        ('1', 'General'),
        ('2', 'OBC'),
        ('3', 'SC'),
        ('4', 'ST'),
    )
    HOSTELS = (
        ('1', 'B1'),
        ('2', 'B2'),
        ('3', 'G6'),
        ('4', 'G5'),
    )
    NATION = (
        ('1', 'Indian'),
        ('2', 'Other'),
    )
    # Validators

    # Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=8)
    year = models.SmallIntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    gpa = models.FloatField()
    phone = models.CharField(max_length=15)
    parent_name = models.CharField(max_length=30)
    dob = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORY)
    blood_group = models.CharField(max_length=5)  # Choices
    jee_air = models.IntegerField()
    hostel_name = models.CharField(max_length=2, choices=HOSTELS, blank=True)
    room_no = models.SmallIntegerField()
    hobbies = models.TextField()
    physical_disability = models.BooleanField(default=False)
    nationality = models.CharField(max_length=10, choices=NATION)
    permanent_address = models.TextField()
    current_address = models.TextField()
    x_year = models.SmallIntegerField()
    x_board_name = models.CharField(max_length=30)
    x_percentage = models.CharField(max_length=10)
    xii_year = models.SmallIntegerField()
    xii_board_name = models.CharField(max_length=30)
    xii_percentage = models.CharField(max_length=10)

    def __str__(self):
        return self.user.get_full_name()


class CompanyProfile(models.Model):
    # Choices
    NATION = (
        ('1', 'Indian'),
        ('2', 'Other'),
    )
    # Model
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    domain = models.CharField(max_length=30, help_text="Type of company like banking/consulting etc ")  # add choices
    url = models.URLField()
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=15, choices=NATION)
    pin_code = models.CharField(max_length=15, blank=True)
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

    def __str__(self):
        return self.student.user.get_full_name()
