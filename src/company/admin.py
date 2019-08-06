from django.contrib import admin
from .models import JobAdvertisement, InternshipAdvertisement, InternshipOffer, JobOffer
from django.shortcuts import HttpResponseRedirect
from zipfile import ZipFile
from os.path import basename
from import_export.admin import ImportExportActionModelAdmin
from .resources import JobOfferResource, InternshipOfferResource, JobAdvertisementResource, \
    InternshipAdvertisementResource


def get_zipped_resumes(modeladmin, request, queryset):
    if queryset.count() != 1:
        modeladmin.message_user(request, "Can not export more than one object to zip at once.")
        return
    if modeladmin.model is JobAdvertisement:
        offers = JobOffer.objects.filter(profile__in=queryset).all()
    elif modeladmin.model is InternshipAdvertisement:
        offers = InternshipOffer.objects.filter(profile__in=queryset).all()
    if not offers.count():
        modeladmin.message_user(request, "No offers exist for this advertisement")
        return

    zip_path = "resume/zipped/" + offers[0].profile.company.name + '  ' + offers[0].profile.designation + '  ' + str(
        offers[0].profile_id) + ".zip"

    zip = ZipFile(zip_path, 'w')
    for offer in offers:
        zip.write(offer.resume.file.path, basename(offer.resume.file.path))

    zip.close()
    url = "/media/" + zip_path
    return HttpResponseRedirect(url)


def make_active(modeladmin, request, queryset):
    queryset.update(active=True)


def make_inactive(modeladmin, request, queryset):
    queryset.update(active=False)


def mark_placed(modeladmin, request, queryset):
    queryset.update(is_accepted=True)


def mark_ppo(modeladmin, request, queryset):
    queryset.update(ppo=True)
    queryset.update(is_accepted=True)


@admin.register(JobAdvertisement)
class JobAdvertisementAdmin(ImportExportActionModelAdmin):
    readonly_fields = ['creation_timestamp', ]
    resource_class = JobAdvertisementResource
    list_display = ['company', 'designation', 'ctc', 'min_gpa', 'active', 'expiry', ]
    list_filter = ['company', 'active', 'creation_timestamp', ]
    ordering = ['company']
    search_fields = ['company__name', ]
    actions = [get_zipped_resumes, make_active, make_inactive]

    class Meta:
        model = JobAdvertisement
        fields = '__all__'


@admin.register(InternshipAdvertisement)
class InternshipAdvertisementAdmin(ImportExportActionModelAdmin):
    readonly_fields = ['creation_timestamp', ]
    resource_class = InternshipAdvertisementResource
    list_display = ['company', 'designation', 'min_gpa', 'ctc', 'active', 'expiry', ]
    list_filter = ['company', 'active', 'creation_timestamp', ]
    ordering = ['company']
    search_fields = ['company__name', ]
    actions = [get_zipped_resumes, make_active, make_inactive]

    class Meta:
        model = InternshipAdvertisement
        fields = '__all__'


@admin.register(InternshipOffer)
class InternshipOfferAdmin(ImportExportActionModelAdmin):
    readonly_fields = ['application_timestamp', ]
    resource_class = InternshipOfferResource
    list_display = ['student', 'company', 'profile', 'is_accepted', 'get_file']
    list_filter = ['company', 'is_accepted', 'profile']
    ordering = ['student']
    search_fields = ['company__name', 'student__user__username', 'student__user__first_name',
                     'student__user__last_name', ]
    actions = [mark_placed, mark_ppo]

    class Meta:
        model = InternshipOffer
        fields = '__all__'


@admin.register(JobOffer)
class JobOfferAdmin(ImportExportActionModelAdmin):
    readonly_fields = ['application_timestamp', ]
    resource_class = JobOfferResource
    list_display = ['student', 'company', 'profile', 'is_accepted', 'get_file']
    list_filter = ['company', 'is_accepted', 'profile']
    ordering = ['student']
    search_fields = ['company__name', 'student__user__username', 'student__user__first_name',
                     'student__user__last_name', ]
    actions = [mark_placed, mark_ppo]

    class Meta:
        model = JobOffer
        fields = '__all__'
