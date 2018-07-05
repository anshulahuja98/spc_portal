from django.contrib import admin
from .models import JobAdvertisement, InternshipAdvertisement


@admin.register(JobAdvertisement)
class JobAdvertisementAdmin(admin.ModelAdmin):
    class Meta:
        model = JobAdvertisement
        fields = '__all__'


@admin.register(InternshipAdvertisement)
class InternshipAdvertisementAdmin(admin.ModelAdmin):
    class Meta:
        model = InternshipAdvertisement
        fields = '__all__'
