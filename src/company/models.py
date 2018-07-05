from django.db import models
from uuid import uuid4
from django.shortcuts import reverse
from accounts.models import CompanyProfile, StudentProfile
from student.models import Branch, Program


class BaseAdvertisement(models.Model):
    # job prof
    id = models.UUIDField(primary_key=True, default=uuid4)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    tentative_join_date = models.DateField()
    tentative_job_location = models.CharField(max_length=50)
    ads = models.FileField(upload_to='ads', null=True, blank=True)
    # package details
    ctc = models.FloatField()
    gross_salary = models.FloatField()
    bonus = models.PositiveIntegerField(blank=True, default=0)
    bond = models.BooleanField()
    # selection process
    eligible_branches = models.ManyToManyField(Branch, default=Branch.objects.all())
    eligible_programs = models.ManyToManyField(Program, default=Branch.objects.all())
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
    other_details = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{} ({})".format(self.designation, self.company.name)

    def get_absolute_url(self):
        return reverse("company:offer", kwargs={"id": self.id})


class JobAdvertisement(BaseAdvertisement):
    pass


class InternshipAdvertisement(BaseAdvertisement):
    pass


class BaseOffer(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)

    @property
    def ctc(self):
        return self.profile.ctc

    def __str__(self):
        return "{} ({}) - {}".format(self.student.user.get_full_name(), self.profile.designation,
                                     self.company.name)

    class Meta:
        abstract = True


class JobOffer(BaseOffer):
    profile = models.ForeignKey(JobAdvertisement, on_delete=models.CASCADE)


class InternshipOffer(BaseOffer):
    profile = models.ForeignKey(InternshipAdvertisement, on_delete=models.CASCADE)
