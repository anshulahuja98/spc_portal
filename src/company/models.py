from django.db import models
from uuid import uuid4
from django.shortcuts import reverse
from accounts.models import CompanyProfile, StudentProfile, Resume
from student.models import ProgramAndBranch
from django.db.models.signals import pre_save


class BaseAdvertisement(models.Model):
    # validity
    expiry = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=False)
    # job prof
    id = models.UUIDField(primary_key=True, default=uuid4)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    designation = models.CharField(max_length=250)
    description = models.TextField()
    tentative_join_date = models.DateField()
    tentative_job_location = models.CharField(max_length=50)
    ads = models.FileField(upload_to='ads', null=True, blank=True)
    # package details
    ctc = models.FloatField()
    gross_salary = models.FloatField(null=True, blank=True)
    bonus = models.CharField(blank=True, null=True, max_length=100)
    bond = models.BooleanField()
    bond_details = models.TextField(blank=True, null=True)
    # selection process
    eligible_program_branch = models.ManyToManyField(ProgramAndBranch, default=ProgramAndBranch.objects.all())
    resume_required = models.BooleanField()
    resume_shortlist_criteria = models.TextField(null=True, blank=True)
    aptitude_test_required = models.BooleanField()
    group_discussion_required = models.BooleanField()
    number_of_technical_interviews = models.PositiveSmallIntegerField(default=0)
    number_of_technical_tests = models.PositiveSmallIntegerField(default=0)
    number_of_hr_rounds = models.PositiveSmallIntegerField(default=0)
    medical_test_required = models.BooleanField()
    min_gpa = models.FloatField()
    number_of_members = models.PositiveIntegerField(null=True, blank=True)
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
    ppo = models.BooleanField(default=False)
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True)
    date_time = models.DateField(auto_created=True)

    @property
    def ctc(self):
        return self.profile.ctc

    def __str__(self):
        return "{} ({}) - {}".format(self.student.user.username, self.profile.designation,
                                     self.company.name, self.date_time)

    class Meta:
        abstract = True

    def get_file(self):
        if self.resume and self.resume.file:
            return self.resume.file
        else:
            return 'None'


class JobOffer(BaseOffer):
    profile = models.ForeignKey(JobAdvertisement, on_delete=models.CASCADE)


class InternshipOffer(BaseOffer):
    profile = models.ForeignKey(InternshipAdvertisement, on_delete=models.CASCADE)


def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.company:
        instance.company = instance.profile.company
    if instance.ppo and not instance.is_accepted:
        instance.is_accepted = True


pre_save.connect(event_pre_save_receiver, sender=InternshipOffer)

pre_save.connect(event_pre_save_receiver, sender=JobOffer)
