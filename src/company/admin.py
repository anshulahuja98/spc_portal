from django.contrib import admin
from .models import JobAdvertisement, InternAdvertisement, JobOffer, InterOffer


class JobAdvertisementInline(admin.StackedInline):
    model = JobAdvertisement


class InternAdvertisementInline(admin.StackedInline):
    model = InternAdvertisement


@admin.register(JobAdvertisement)
class JobOfferAdmin(admin.ModelAdmin):
    inlines = (JobAdvertisementInline,)

    class Meta:
        model = JobOffer
        fields = '__all__'


@admin.register(InternAdvertisement)
class InternOfferAdmin(admin.ModelAdmin):
    inlines = (InternAdvertisementInline,)

    class Meta:
        model = InterOffer
        fields = '__all__'
