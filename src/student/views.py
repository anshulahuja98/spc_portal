from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, ListView, TemplateView
from accounts.models import StudentProfile, Resume
from company.models import JobOffer,InternOffer
from django.shortcuts import get_object_or_404


class UserObjectMixin(object):
    def get_object(self):
        return get_object_or_404(StudentProfile, user=self.request.user)


class LoginView(DefaultLoginView):
    template_name = 'student/login.html'


class DetailsView(UpdateView, LoginRequiredMixin, UserObjectMixin):
    # template_name = 'student/details.html'
    model = StudentProfile
    fields = '__all__'
    template_name = 'student/details.html'

    def get_object(self):
        return get_object_or_404(StudentProfile, user=self.request.user)


class JobOffersListView(ListView, LoginRequiredMixin):
    model = JobOffer
    template_name = 'student/job_offers.html'

    def get_queryset(self):
        return self.model.objects

class InternOffersListView(ListView, LoginRequiredMixin):
    model = InternOffer
    template_name = 'student/intern_offers.html'

    def get_queryset(self):
        return self.model.objects


class ResumeUploadView(UpdateView):
    model = Resume
