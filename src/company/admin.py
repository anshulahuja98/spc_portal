from django.contrib import admin
from .models import JobAdvertisement, InternshipAdvertisement, InternshipOffer, JobOffer
from django.shortcuts import HttpResponseRedirect
from zipfile import ZipFile
from os.path import basename
from import_export.admin import ImportExportActionModelAdmin
from .resources import JobOfferResource, InternshipOfferResource, JobAdvertisementResource, \
    InternshipAdvertisementResource
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


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


def send_email(self, request, obj, subject):
    if "_sendemail" in request.POST:
        obj.email_sent = True
        obj.save()
        from_email = settings.EMAIL_HOST_USER
        to_email = []
        for email_id in obj.email_ids.all():
            to_email.append(email_id.email)
        html_content = render_to_string("company/ad_email.html", {'subject': subject,
                                                                  'company': obj.company,
                                                                  'designation': obj.designation,
                                                                  'description': obj.description,
                                                                  'tentative_join_date': obj.tentative_join_date,
                                                                  'tentative_job_location': obj.tentative_job_location,
                                                                  'ads': obj.ads.url,
                                                                  'ctc': obj.ctc,
                                                                  'gross_salary': obj.gross_salary,
                                                                  'bonus': obj.bonus,
                                                                  'bond': obj.bond,
                                                                  'bond_details': obj.bond_details,
                                                                  'resume_required': obj.resume_required,
                                                                  'resume_shortlist_criteria': obj.resume_shortlist_criteria,
                                                                  'aptitude_test_required': obj.aptitude_test_required,
                                                                  'group_discussion_required': obj.group_discussion_required,
                                                                  'number_of_technical_interviews': obj.number_of_technical_interviews,
                                                                  'number_of_technical_tests': obj.number_of_technical_tests,
                                                                  'number_of_hr_rounds': obj.number_of_hr_rounds,
                                                                  'medical_test_required': obj.medical_test_required,
                                                                  'min_gpa': obj.min_gpa,
                                                                  'number_of_members': obj.number_of_members,
                                                                  'other_details': obj.other_details,
                                                                  'expiry': obj.expiry})
        text_content = strip_tags(html_content)
        message = EmailMultiAlternatives(subject=subject, body=text_content, from_email=from_email, to=to_email)
        message.attach_alternative(html_content, "text/html")
        message.send()
        self.message_user(request, "Email Sent")
        return HttpResponseRedirect(".")


@admin.register(JobAdvertisement)
class JobAdvertisementAdmin(ImportExportActionModelAdmin):
    change_form_template = "admin/adversiment_change_form.html"
    resource_class = JobAdvertisementResource
    list_display = ['company', 'designation', 'ctc', 'min_gpa', 'active', 'expiry', 'email_sent']
    list_filter = ['company', 'active', ]
    ordering = ['company']
    search_fields = ['company__name', ]
    actions = [get_zipped_resumes, make_active, make_inactive]

    def response_change(self, request, obj):
        subject = "Job Advertisement"
        send_email(self, request, obj, subject)
        return super().response_change(request, obj)

    class Meta:
        model = JobAdvertisement
        fields = '__all__'


@admin.register(InternshipAdvertisement)
class InternshipAdvertisementAdmin(ImportExportActionModelAdmin):
    change_form_template = "admin/adversiment_change_form.html"
    resource_class = InternshipAdvertisementResource
    list_display = ['company', 'designation', 'min_gpa', 'ctc', 'active', 'expiry', 'email_sent']
    list_filter = ['company', 'active', ]
    ordering = ['company']
    search_fields = ['company__name', ]
    actions = [get_zipped_resumes, make_active, make_inactive]

    def response_change(self, request, obj):
        subject = "Internship Advertisement"
        send_email(self, request, obj, subject)
        return super().response_change(request, obj)

    class Meta:
        model = InternshipAdvertisement
        fields = '__all__'


@admin.register(InternshipOffer)
class InternshipOfferAdmin(ImportExportActionModelAdmin):
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
