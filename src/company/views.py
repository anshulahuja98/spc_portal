from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from .forms import JobOfferForm, InternOfferForm


class LoginView(DefaultLoginView):
    template_name = 'company/login.html'


class JobOfferFormView(FormView, LoginRequiredMixin):
    form_class = JobOfferForm
    template_name = 'company/joboffer.html'


class InternOfferFormView(FormView, LoginRequiredMixin):
    form_class = InternOfferForm
    template_name = 'company/internoffer.html'

