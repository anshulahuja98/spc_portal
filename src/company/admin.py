from django.contrib import admin
from .models import InternOffer, JobOffer


@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    class Meta:
        model = JobOffer
        fields = '__all__'


@admin.register(InternOffer)
class InternOfferAdmin(admin.ModelAdmin):
    class Meta:
        model = InternOffer
        fields = '__all__'
