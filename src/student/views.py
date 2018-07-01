from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView
from accounts.models import StudentProfile
from company.models import JobProfile, InternshipProfile
from django.shortcuts import get_object_or_404


class DetailsView(LoginRequiredMixin, UpdateView):
    # template_name = 'student/details.html'
    model = StudentProfile
    fields = '__all__'
    template_name = 'student/details.html'

    def get_object(self, queryset=None):
        return get_object_or_404(StudentProfile, user=self.request.user)


class JobOffersListView(LoginRequiredMixin, ListView):
    model = JobProfile
    template_name = 'student/job_offers.html'

    def get_queryset(self):
        return self.model.objects


class InternOffersListView(LoginRequiredMixin, ListView):
    model = InternshipProfile
    template_name = 'student/intern_offers.html'

    def get_queryset(self):
        return self.model.objects


class ResumeUploadView(LoginRequiredMixin, UpdateView):
    model = StudentProfile
    template_name = 'student/resume.html'
    fields = ('resume_1', 'resume_2', 'resume_3', 'resume_4', 'resume_5',)

    def get_object(self, queryset=None):
        return get_object_or_404(StudentProfile, user=self.request.user)
