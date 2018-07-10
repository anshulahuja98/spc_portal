from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, DetailView
from .forms import JobAdvertisementForm, InternshipAdvertisementForm
from company.models import JobAdvertisement, InternshipAdvertisement
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.shortcuts import get_object_or_404, reverse, HttpResponseRedirect
from accounts.models import CompanyProfile


class LoginView(DefaultLoginView):
    template_name = 'company/login.html'


class JobAdvertisementFormView(FormView, LoginRequiredMixin):
    form_class = JobAdvertisementForm
    template_name = 'company/joboffer_form.html'
    success_url = '/company/job_offers/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

    def post(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        self.request.POST.update({
            'company': CompanyProfile.objects.get(user=self.request.user).id,
        })
        self.request.POST._mutable = False
        return super().post(request, args, kwargs)


class InternshipAdvertisementFormView(FormView, LoginRequiredMixin):
    form_class = InternshipAdvertisementForm
    template_name = 'company/internoffer_form.html'
    success_url = '/company/intern_offers/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

    def post(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        self.request.POST.update({
            'company': CompanyProfile.objects.get(user=self.request.user).id,
        })
        self.request.POST._mutable = False
        return super().post(request, args, kwargs)


class JobAdvertisementsAddedListView(ListView):
    model = JobAdvertisement
    template_name = 'company/job_offers.html'
    context_object_name = 'job_ad_list'

    def get_queryset(self):
        return self.model.objects.filter(company__user=self.request.user)


class InternshipAdvertisementAddedListView(ListView):
    model = InternshipAdvertisement
    template_name = 'company/intern_offers.html'
    context_object_name = 'intern_ad_list'

    def get_queryset(self):
        return self.model.objects.filter(company__user=self.request.user)


class OfferView(LoginRequiredMixin, DetailView):
    model = InternshipAdvertisement
    template_name = 'company/offer.html'
    context_object_name = 'ad'

    def get_object(self, queryset=None):
        return get_object_or_404(InternshipAdvertisement, id=self.kwargs.get('id'))
