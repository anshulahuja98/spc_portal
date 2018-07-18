from django.db import models
from uuid import uuid4
from django.shortcuts import reverse
from accounts.models import CompanyProfile, StudentProfile, Resume
from student.models import ProgramAndBranch
from django.db.models.signals import pre_save


class BaseAdvertisement(models.Model):
    # job prof
    id = models.UUIDField(primary_key=True, default=uuid4)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30)
    description = models.TextField()
    tentative_join_date = models.DateField()
    tentative_job_location = models.CharField(max_length=50)
    ads = models.FileField(upload_to='ads', null=True, blank=True)
    # package details
    ctc = models.FloatField()
    gross_salary = models.FloatField()
    bonus = models.PositiveIntegerField(blank=True, default=0, null=True)
    bond = models.BooleanField()
    # selection process
    eligible_program_branch = models.ManyToManyField(ProgramAndBranch, default=ProgramAndBranch.objects.all())
    # eligible_programs = models.ManyToManyField(Program, default=ProgramAndBranch.objects.all())
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


class JobAdvertisement(BaseAdvertisement):
    pass

    def get_absolute_url(self):
        return reverse("company:job-offer", kwargs={"id": self.id})

    def get_offers(self):
        return JobOffer.objects.filter(profile__id=self.id)


class InternshipAdvertisement(BaseAdvertisement):
    pass

    def get_absolute_url(self):
        return reverse("company:internship-offer", kwargs={"id": self.id})

    def get_offers(self):
        return InternshipOffer.objects.filter(profile__id=self.id)


class BaseOffer(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(CompanyProfile, on_delete=models.SET_NULL, null=True)
    is_accepted = models.BooleanField(default=False)
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True)

    @property
    def ctc(self):
        return self.profile.ctc

    def __str__(self):
        return "{} ({}) - {}".format(self.student.user.username, self.profile.designation,
                                     self.company.name)

    class Meta:
        abstract = True


class JobOffer(BaseOffer):
    profile = models.ForeignKey(JobAdvertisement, on_delete=models.CASCADE)


class InternshipOffer(BaseOffer):
    profile = models.ForeignKey(InternshipAdvertisement, on_delete=models.CASCADE)


def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.company:
        instance.company = instance.profile.company


pre_save.connect(event_pre_save_receiver, sender=InternshipOffer)

pre_save.connect(event_pre_save_receiver, sender=JobOffer)
