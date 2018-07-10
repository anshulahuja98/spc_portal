from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, DetailView
from .forms import JobAdvertisementForm, InternshipAdvertisementForm
from company.models import JobAdvertisement, InternshipAdvertisement
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.shortcuts import get_object_or_404, reverse


class LoginView(DefaultLoginView):
    template_name = 'company/login.html'


class JobAdvertisementFormView(FormView, LoginRequiredMixin):
    form_class = JobAdvertisementForm
    template_name = 'company/joboffer_form.html'


class InternshipAdvertisementFormView(FormView, LoginRequiredMixin):
    form_class = InternshipAdvertisementForm
    template_name = 'company/internoffer_form.html'

    def get_success_url(self):
        return reverse('company:intern-offer-form')


class JobProfilesAddedListView(ListView):
    model = JobAdvertisement
    template_name = 'company/job_offers.html'

    def get_queryset(self):
        return self.model.objects.filter(company__user=self.request.user)


class InternshipProfilesAddedListView(ListView):
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
