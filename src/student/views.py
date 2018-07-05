from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView, DetailView, FormView
from accounts.models import StudentProfile, Resume
from company.models import JobAdvertisement, InternshipAdvertisement
from django.shortcuts import get_object_or_404
from accounts.forms import ResumeForm


class DetailsView(LoginRequiredMixin, UpdateView):
    model = StudentProfile
    fields = ('roll_no','branch','program','gpa','phone','parent_name','dob','category','blood_group','jee_air',)
    # fields = ('roll_no',)
    # fields = '__all__'
    template_name = 'student/details.html'
    success_url = '/student/details/'

    def get_object(self, queryset=None):
        return get_object_or_404(StudentProfile, user=self.request.user)


class JobOffersListView(LoginRequiredMixin, ListView):
    model = JobAdvertisement
    context_object_name = 'job_ad_list'
    template_name = 'student/job_offers.html'

    def get_queryset(self):
        profile = get_object_or_404(StudentProfile, user=self.request.user)
        return self.model.objects.filter(min_gpa__lte=profile.gpa)


class InternOffersListView(LoginRequiredMixin, ListView):
    model = InternshipAdvertisement
    template_name = 'student/intern_offers.html'
    context_object_name = 'intern_ad_list'

    def get_queryset(self):
        return self.model.objects.all()


# class ResumeUploadView(LoginRequiredMixin, UpdateView):
#     model = Resume
#     template_name = 'student/resume.html'
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(Resume, student__user=self.request.user)
#


class ResumeUploadView(FormView):
    ResumeFormSet = forms.formset_factory(ResumeForm, extra=4)
    template_name = 'student/resume.html'
    resume_formset = ResumeFormSet(prefix='resume')
    model = Resume
