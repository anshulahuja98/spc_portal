from django.contrib import admin
from .models import JobAdvertisement, InternAdvertisement


@admin.register(JobAdvertisement)
class JobOfferAdmin(admin.ModelAdmin):
    class Meta:
        model = JobAdvertisement
        fields = '__all__'


@admin.register(InternAdvertisement)
class InternOfferAdmin(admin.ModelAdmin):
    class Meta:
        model = InternAdvertisement
        fields = '__all__'
