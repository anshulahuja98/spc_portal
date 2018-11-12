from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView, FormView, CreateView, View
from accounts.models import StudentProfile, Resume
from company.models import JobAdvertisement, InternshipAdvertisement, JobOffer, InternshipOffer
from django.shortcuts import get_object_or_404
from accounts.forms import ResumeForm
from .forms import InternshipOfferForm, JobOfferForm
from django.shortcuts import HttpResponseRedirect


class StudentProfileRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'studentprofile'):
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()


class DetailsView(StudentProfileRequiredMixin, UpdateView):
    model = StudentProfile
    fields = (
        'roll_no', 'program_branch', 'gpa', 'phone', 'dob', 'category', 'jee_air',
        'x_year', 'x_board_name', 'x_percentage', 'xii_year', 'xii_board_name', 'xii_percentage',
        'current_address', 'permanent_address', 'nationality', 'physical_disability',
    )
    template_name = 'student/details.html'
    success_url = '/student/details/'

    def get_object(self, queryset=None):
        return get_object_or_404(StudentProfile, user=self.request.user)


class JobOfferApplyFormView(StudentProfileRequiredMixin, CreateView):
    template_name = 'student/offers_list.html'
    form_class = JobOfferForm
    success_url = '/student/job_offers/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

    def post(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        self.request.POST.update({
            'student': StudentProfile.objects.get(user=self.request.user).id,
        })
        self.request.POST._mutable = False
        return super().post(request, args, kwargs)

    def get_form_kwargs(self):
        kwargs = super(JobOfferApplyFormView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class JobOffersListView(StudentProfileRequiredMixin, ListView):
    model = JobAdvertisement
    template_name = 'student/offers_list.html'
    context_object_name = 'ad_list'

    def get_queryset(self):
        profile = get_object_or_404(StudentProfile, user=self.request.user)
        return self.model.objects.filter(min_gpa__lte=profile.gpa,
                                         eligible_program_branch__name__contains=profile.program_branch.name,
                                         active=True).difference(self.get_applied_ad_list())

    def get_context_data(self, **kwargs):
        context = super(JobOffersListView, self).get_context_data(**kwargs)
        context['form'] = JobOfferForm(user=self.request.user)
        context['applied_offer_list'] = self.get_applied_offer_list()
        context['userprofile'] = StudentProfile.objects.get(user=self.request.user)
        return context

    def get_applied_ad_list(self):
        return JobAdvertisement.objects.filter(
            id__in=JobOffer.objects.filter(student__user=self.request.user).values_list('profile'))

    def get_applied_offer_list(self):
        return JobOffer.objects.filter(student__user=self.request.user)


class JobOffersView(StudentProfileRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = JobOffersListView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = JobOfferApplyFormView.as_view()
        return view(request, *args, **kwargs)


class InternshipOffersListView(StudentProfileRequiredMixin, ListView):
    model = InternshipAdvertisement
    template_name = 'student/offers_list.html'
    context_object_name = 'ad_list'

    def get_queryset(self):
        profile = get_object_or_404(StudentProfile, user=self.request.user)
        username = self.request.user.username
        if username[0] is 'M' and username[2] is '8':
            return self.model.objects.filter(
                eligible_program_branch__name__contains=profile.program_branch.name,
                active=True).difference(self.get_applied_ad_list())
        else:
            return self.model.objects.filter(min_gpa__lte=profile.gpa,
                                             eligible_program_branch__name__contains=profile.program_branch.name,
                                             active=True).difference(self.get_applied_ad_list())

    def get_context_data(self, **kwargs):
        context = super(InternshipOffersListView, self).get_context_data(**kwargs)
        context['form'] = InternshipOfferForm(user=self.request.user)
        context['applied_offer_list'] = self.get_applied_offer_list()
        context['userprofile'] = StudentProfile.objects.get(user=self.request.user)
        return context

    def get_applied_ad_list(self):
        return InternshipAdvertisement.objects.filter(
            id__in=InternshipOffer.objects.filter(student__user=self.request.user).values_list('profile'))

    def get_applied_offer_list(self):
        return InternshipOffer.objects.filter(student__user=self.request.user)


class InternshipOfferApplyFormView(StudentProfileRequiredMixin, CreateView):
    template_name = 'student/offers_list.html'
    form_class = InternshipOfferForm
    success_url = '/student/intern_offers/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

    def post(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        self.request.POST.update({
            'student': StudentProfile.objects.get(user=self.request.user).id,
        })
        self.request.POST._mutable = False
        return super().post(request, args, kwargs)

    def get_form_kwargs(self):
        kwargs = super(InternshipOfferApplyFormView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class InternshipOffersView(StudentProfileRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = InternshipOffersListView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = InternshipOfferApplyFormView.as_view()
        return view(request, *args, **kwargs)


class ResumeListView(StudentProfileRequiredMixin, ListView):
    model = Resume
    template_name = 'student/resume.html'
    context_object_name = 'resume_list'

    def get_queryset(self):
        profile = get_object_or_404(StudentProfile, user=self.request.user)
        return self.model.objects.filter(student=profile)


class ResumeUploadFormView(StudentProfileRequiredMixin, FormView):
    model = Resume
    template_name = 'student/resume.html'
    form_class = ResumeForm
    success_url = '/student/resume_upload/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

    def post(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        self.request.POST.update({
            'student': StudentProfile.objects.get(user=self.request.user).id,
        })
        self.request.POST._mutable = False
        return super().post(request, args, kwargs)


class ResumeView(StudentProfileRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = ResumeListView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ResumeUploadFormView.as_view()
        return view(request, *args, **kwargs)
