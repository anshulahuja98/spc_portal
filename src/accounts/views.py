from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import reverse
from .models import CompanyProfile
from .forms import StudentRegisterForm,CompanyRegisterForm


class StudentRegisterView(CreateView):
    form_class = StudentRegisterForm
    template_name = 'student/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()
        StudentRegisterView.create_profile(user, **form.cleaned_data)
        return super(StudentRegisterView, self).form_valid(form)

    @staticmethod
    def create_profile(user=None, **kwargs):
        # Creates a new UserProfile object after successful creation of User object
        userprofile = CompanyProfile.objects.create(user=user, )
        userprofile.save()


class CompanyRegisterView(CreateView):
    form_class = CompanyRegisterForm
    template_name = 'company/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()
        CompanyRegisterView.create_profile(user, **form.cleaned_data)
        return super(CompanyRegisterView, self).form_valid(form)

    @staticmethod
    def create_profile(user=None, **kwargs):
        # Creates a new UserProfile object after successful creation of User object
        userprofile = CompanyProfile.objects.create(user=user, )
        userprofile.save()
