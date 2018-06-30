from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, ListView, FormView
from accounts.models import StudentProfile
from company.models import JobOffer


# class JobOfferFormView(FormView,LoginRequiredMixin):
#     form_class = JobOfferForm
#
# class InternOfferFormView(FormView,LoginRequiredMixin):
#     form_class = InternOfferForm
