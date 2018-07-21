from django.contrib import admin
from company.models import JobOffer, InternshipOffer, JobAdvertisement, InternshipAdvertisement
from accounts.models import StudentProfile, CompanyPerson, CompanyProfile, Resume


class JobAdvertisementInline(admin.StackedInline):
    model = JobAdvertisement


class InternshipAdvertisementInline(admin.StackedInline):
    model = InternshipAdvertisement


class JobOfferInline(admin.StackedInline):
    model = JobOffer


class InternshipOfferInline(admin.StackedInline):
    model = InternshipOffer


class CompanyPersonInline(admin.StackedInline):
    model = CompanyPerson


class ResumeInline(admin.StackedInline):
    model = Resume


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    inlines = (ResumeInline,)
    list_display = ['__str__', 'roll_no', 'program_branch', 'year']
    list_filter = ['program_branch', 'year']
    ordering = ['roll_no', ]

    class Meta:
        model = StudentProfile
        fields = '__all__'


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    inlines = (CompanyPersonInline, JobOfferInline, InternshipOfferInline,)
    list_display = ['name', 'domain', 'url', ]
    list_filter = ['domain', ]

    class Meta:
        model = CompanyProfile
        fields = '__all__'


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['student', 'is_verified', ]
    list_filter = ['student', ]

    class Meta:
        model = Resume
        fields = '__all__'
