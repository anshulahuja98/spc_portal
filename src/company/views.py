from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, DetailView
from .forms import JobOfferForm, InternOfferForm
from company.models import JobAdvertisement, InternshipAdvertisement
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.shortcuts import get_object_or_404


class LoginView(DefaultLoginView):
    template_name = 'company/login.html'


class JobOfferFormView(FormView, LoginRequiredMixin):
    form_class = JobOfferForm
    template_name = 'company/joboffer_form.html'


class InternOfferFormView(FormView, LoginRequiredMixin):
    form_class = InternOfferForm
    template_name = 'company/internoffer_form.html'


class JobProfilesAddedListView(ListView):
    model = JobAdvertisement
    template_name = 'company/job_offers.html'

    def get_queryset(self):
        return self.model.objects.filter(company__user=self.request.user)


class InternProfilesAddedListView(ListView):
    model = InternshipAdvertisement
    template_name = 'company/intern_offers.html'

    def get_queryset(self):
        return self.model.objects.filter(company__user=self.request.user)


class OfferView(LoginRequiredMixin, DetailView):
    model = InternshipAdvertisement
    template_name = 'company/offer.html'
    context_object_name = 'ad'

    def get_object(self, queryset=None):
        return get_object_or_404(InternshipAdvertisement, id=self.kwargs.get('id'))
