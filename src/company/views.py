from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView
from .forms import JobOfferForm, InternOfferForm
from django.contrib.auth.views import LoginView as DefaultLoginView

class LoginView(DefaultLoginView):
    template_name = 'company/login.html'


class JobOfferFormView(FormView, LoginRequiredMixin):
    form_class = JobOfferForm
    template_name = 'company/joboffer_form.html'


class InternOfferFormView(FormView, LoginRequiredMixin):
    form_class = InternOfferForm
    template_name = 'company/internoffer_form.html'


class JobOffersAddedListView(ListView):
    model = JobOffer
    template_name = 'company/job_offers.html'

    def get_queryset(self):
        return self.model.objects.filter(company__user=self.request.user)


class InternOffersAddedListView(ListView):
    model = InternOffer
    template_name = 'company/intern_offers.html'

    def get_queryset(self):
        return self.model.objects.filter(company__user=self.request.user)
