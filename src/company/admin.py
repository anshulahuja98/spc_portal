from django.contrib import admin
from .models import JobAdvertisement, InternshipAdvertisement, InternshipOffer, JobOffer


@admin.register(JobAdvertisement)
class JobAdvertisementAdmin(admin.ModelAdmin):
    list_display = ['company', 'designation', 'ctc', 'active', 'expiry', ]
    list_filter = ['company', 'active', ]
    ordering = ['company']

    class Meta:
        model = JobAdvertisement
        fields = '__all__'


@admin.register(InternshipAdvertisement)
class InternshipAdvertisementAdmin(admin.ModelAdmin):
    list_display = ['company', 'designation', 'ctc', 'active', 'expiry', ]
    list_filter = ['company', 'active', ]
    ordering = ['company']

    class Meta:
        model = InternshipAdvertisement
        fields = '__all__'


@admin.register(InternshipOffer)
class InternshipOfferAdmin(admin.ModelAdmin):
    list_display = ['student', 'company', 'profile', 'is_accepted', ]
    list_filter = ['company', 'is_accepted', 'student']
    ordering = ['student']

    class Meta:
        model = InternshipOffer
        fields = '__all__'


@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = ['student', 'company', 'profile', 'is_accepted', ]
    list_filter = ['company', 'is_accepted', 'student']
    ordering = ['student']

    class Meta:
        model = JobOffer
        fields = '__all__'
