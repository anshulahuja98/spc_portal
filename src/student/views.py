from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView, FormView, CreateView, View
from accounts.models import StudentProfile, Resume
from company.models import JobAdvertisement, InternshipAdvertisement
from django.shortcuts import get_object_or_404
from accounts.forms import ResumeForm
from .forms import InternshipOfferForm, JobOfferForm
from django.shortcuts import HttpResponseRedirect


class DetailsView(LoginRequiredMixin, UpdateView):
    model = StudentProfile
    fields = (
        'roll_no', 'program_branch', 'gpa', 'phone', 'parent_name', 'dob', 'category', 'blood_group', 'jee_air',
        'x_year', 'x_board_name', 'x_percentage', 'xii_year', 'xii_board_name', 'xii_percentage',
        'current_address', 'permanent_address', 'nationality', 'physical_disability', 'hobbies', 'room_no',
        'hostel_name')
    template_name = 'student/details.html'
    success_url = '/student/details/'

    def get_object(self, queryset=None):
        return get_object_or_404(StudentProfile, user=self.request.user)


# class JobOffersListView(LoginRequiredMixin, ListView):
#     model = JobAdvertisement
#     context_object_name = 'job_ad_list'
#     template_name = 'student/offers_list.html'
#
#     def get_queryset(self):
#         profile = get_object_or_404(StudentProfile, user=self.request.user)
#         return self.model.objects.filter(min_gpa__lte=profile.gpa)


class JobOfferApplyFormView(CreateView):
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


class JobOffersListView(LoginRequiredMixin, ListView):
    model = JobAdvertisement
    template_name = 'student/offers_list.html'
    context_object_name = 'ad_list'

    def get_queryset(self):
        profile = get_object_or_404(StudentProfile, user=self.request.user)
        return self.model.objects.filter(min_gpa__lte=profile.gpa)

    def get_context_data(self, **kwargs):
        context = super(JobOffersListView, self).get_context_data(**kwargs)
        context['form'] = JobOfferForm(user=self.request.user)
        return context


class JobOffersView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = JobOffersListView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = JobOfferApplyFormView.as_view()
        return view(request, *args, **kwargs)


class InternshipOffersListView(LoginRequiredMixin, ListView):
    model = InternshipAdvertisement
    template_name = 'student/offers_list.html'
    context_object_name = 'ad_list'

    def get_queryset(self):
        profile = get_object_or_404(StudentProfile, user=self.request.user)
        return self.model.objects.filter(min_gpa__lte=profile.gpa)


class InternshipOfferApplyFormView(CreateView):
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


class InternshipOffersView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = InternshipOffersListView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = InternshipOfferApplyFormView.as_view()
        return view(request, *args, **kwargs)


class ResumeListView(ListView, LoginRequiredMixin):
    model = Resume
    template_name = 'student/resume.html'
    context_object_name = 'resume_list'

    def get_object(self, queryset=None):
        student = get_object_or_404(StudentProfile, user=self.request.user)
        print(student)
        return self.model.objects.filter(Resume, student=student)


class ResumeUploadFormView(FormView, LoginRequiredMixin):
    model = Resume
    template_name = 'student/resume.html'
    form_class = ResumeForm
    success_url = '/student/resume_upload/'

    def form_valid(self, form):
        print("valid")

    def form_invalid(self, form):
        print("invalid")
        print(form.errors)


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        view = ResumeListView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ResumeUploadFormView.as_view()
        return view(request, *args, **kwargs)

# class ResumeUploadView(FormView):
#     ResumeFormSet = forms.formset_factory(ResumeForm, extra=4)
#     template_name = 'student/resume.html'
#     resume_formset = ResumeFormSet(prefix='resume')
#     model = Resume
