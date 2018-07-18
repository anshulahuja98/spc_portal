from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView, FormView, CreateView, View
from accounts.models import StudentProfile, Resume
from company.models import JobAdvertisement, InternshipAdvertisement, InternshipOffer
from django.shortcuts import get_object_or_404
from accounts.forms import ResumeForm
from .forms import InternshipOfferForm
from django.shortcuts import reverse, HttpResponseRedirect


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


class JobOffersListView(LoginRequiredMixin, ListView):
    model = JobAdvertisement
    context_object_name = 'job_ad_list'
    template_name = 'student/job_offers.html'

    def get_queryset(self):
        profile = get_object_or_404(StudentProfile, user=self.request.user)
        return self.model.objects.filter(min_gpa__lte=profile.gpa)


class InternshipOffersListView(LoginRequiredMixin, ListView):
    model = InternshipAdvertisement
    template_name = 'student/intern_offers.html'
    context_object_name = 'intern_ad_list'

    def get_queryset(self):
        profile = get_object_or_404(StudentProfile, user=self.request.user)
        return self.model.objects.filter(min_gpa__lte=profile.gpa)


class InternshipOfferApplyForm(CreateView):
    template_name = 'student/intern_offers.html'
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
        view = InternshipOfferApplyForm.as_view()
        return view(request, *args, **kwargs)


# class ResumeUploadView(LoginRequiredMixin, UpdateView):
#     model = Resume
#     template_name = 'student/resume.html'
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(Resume, student__user=self.request.user)
#


class ResumeUploadView(FormView):
    ResumeFormSet = forms.formset_factory(ResumeForm, extra=4)
    template_name = 'student/resume.html'
    resume_formset = ResumeFormSet(prefix='resume')
    model = Resume
