from django.contrib import admin
from .models import JobProfile, InternshipProfile, JobOffer, InternshipOffer


@admin.register(JobProfile)
class JobProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = JobProfile
        fields = '__all__'


@admin.register(InternshipProfile)
class InternProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = InternshipProfile
        fields = '__all__'
