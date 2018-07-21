from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, DetailView
from .forms import JobAdvertisementForm, InternshipAdvertisementForm
from company.models import JobAdvertisement, InternshipAdvertisement
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from accounts.models import CompanyProfile


class CompanyProfileRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'companyprofile'):
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()


class JobAdvertisementFormView(CompanyProfileRequiredMixin, FormView):
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


class InternshipAdvertisementFormView(CompanyProfileRequiredMixin, FormView):
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


class JobAdvertisementsAddedListView(CompanyProfileRequiredMixin, ListView):
    model = JobAdvertisement
    template_name = 'company/offers_list.html'
    context_object_name = 'ad_list'

    def get_queryset(self):
        return self.model.objects.filter(company__user=self.request.user)


class InternshipAdvertisementAddedListView(ListView):
    model = InternshipAdvertisement
    template_name = 'company/offers_list.html'
    context_object_name = 'ad_list'

    def get_queryset(self):
        return self.model.objects.filter(company__user=self.request.user)


class InternshipOfferView(CompanyProfileRequiredMixin, DetailView):
    model = InternshipAdvertisement
    template_name = 'company/offer.html'
    context_object_name = 'ad'

    def get_object(self, queryset=None):
        return get_object_or_404(InternshipAdvertisement, id=self.kwargs.get('id'))

    def get_context_data(self, **kwargs):
        context = super(InternshipOfferView, self).get_context_data(**kwargs)
        if hasattr(self.request.user, 'companyprofile'):
            context['base_template'] = 'company/base.html'

        elif hasattr(self.request.user, 'studentprofile'):
            context['base_template'] = 'student/base.html'
        context['type'] = "Internship"
        return context


class JobOfferView(CompanyProfileRequiredMixin, DetailView):
    model = JobAdvertisement
    template_name = 'company/offer.html'
    context_object_name = 'ad'

    def get_object(self, queryset=None):
        return get_object_or_404(JobAdvertisement, id=self.kwargs.get('id'))

    def get_context_data(self, **kwargs):
        context = super(JobOfferView, self).get_context_data(**kwargs)
        if hasattr(self.request.user, 'companyprofile'):
            context['base_template'] = 'company/base.html'

        elif hasattr(self.request.user, 'studentprofile'):
            context['base_template'] = 'student/base.html'
        context['type'] = "Job"
        return context
