from django.db import models
from django.contrib.auth.models import User


class CompanyProfile(models.Model):
    # Choices
    NATION = (
        ('1', 'Indian'),
        ('2', 'Other'),
    )
    # Model
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)  # add choices
    url = models.URLField()
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=15, choices=NATION)
    pincode = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.email


class CompanyPerson(models.Model):
    name = models.CharField(max_length=30)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='persons')
    designation = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()


class Resume(models.Model):
    file = models.FileField(upload_to='resume')
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def verified_status(self):
        return self.verified


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
    cpi = models.FloatField()
    placed_status = models.BooleanField(default=False)
    placed_company = models.ForeignKey(CompanyProfile, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=15)
    parent_name = models.CharField(max_length=30)
    dob = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORY)
    blood_group = models.CharField(max_length=5)  # Choices
    jee_air = models.IntegerField()
    hostel_name = models.CharField(max_length=2, choices=HOSTELS, blank=True)
    room_no = models.SmallIntegerField(blank=True)
    hobbies = models.TextField()
    pd_status = models.BooleanField(default=False)
    nationality = models.CharField(max_length=10, choices=NATION)
    permanent_address = models.TextField()
    current_address = models.TextField()
    x_year = models.SmallIntegerField()
    x_board_name = models.CharField(max_length=30)
    x_percentage = models.CharField(max_length=10)
    xii_year = models.SmallIntegerField()
    xii_board_name = models.CharField(max_length=30)
    xii_percentage = models.CharField(max_length=10)
    ctc = models.IntegerField(null=True, blank=True, )
    resume_1 = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.SET_NULL, related_name='resume_1')
    resume_2 = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.SET_NULL, related_name='resume_2')
    resume_3 = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.SET_NULL, related_name='resume_3')
    resume_4 = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.SET_NULL, related_name='resume_4')
    resume_5 = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.SET_NULL, related_name='resume_5')

    def __str__(self):
        return self.user.username
