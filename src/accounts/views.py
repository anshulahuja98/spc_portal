from django.contrib.auth.views import LoginView as DefaultLoginView
from django.shortcuts import reverse
from django.views.generic import CreateView
from .forms import StudentRegisterForm, CompanyRegisterForm
from accounts.models import StudentProfile, CompanyProfile
from student.models import ProgramAndBranch
from main.views import HomepageView


class LoginView(DefaultLoginView, HomepageView):
    template_name = 'main/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        url = super().get_redirect_url()
        if hasattr(self.request.user, 'companyprofile'):
            return url or reverse('company:job-offers-added')
        elif hasattr(self.request.user, 'studentprofile'):
            return url or reverse('student:detail')
        else:
            return url


class StudentRegisterFormView(CreateView):
    model = StudentProfile
    form_class = StudentRegisterForm
    template_name = 'student/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()
        StudentRegisterFormView.create_profile(user, **form.cleaned_data)
        return super(StudentRegisterFormView, self).form_valid(form)

    @staticmethod
    def create_profile(user=None, **kwargs):
        # Creates a new UserProfile object after successful creation of User object
        userprofile = StudentProfile.objects.create(user=user,
                                                    year=kwargs['year'],
                                                    program_branch=ProgramAndBranch.objects.get(
                                                        abbreviation=kwargs['program_branch']),
                                                    gpa=kwargs['gpa'],
                                                    phone=kwargs['phone'],
                                                    parent_name=kwargs['parent_name'],
                                                    dob=kwargs['dob'],
                                                    category=kwargs['category'],
                                                    blood_group=kwargs['blood_group'],
                                                    jee_air=kwargs['jee_air'],
                                                    hostel_name=kwargs['hostel_name'],
                                                    room_no=kwargs['room_no'],
                                                    hobbies=kwargs['hobbies'],
                                                    physical_disability=kwargs['physical_disability'],
                                                    nationality=kwargs['nationality'],
                                                    permanent_address=kwargs['permanent_address'],
                                                    current_address=kwargs['current_address'],
                                                    x_year=kwargs['x_year'],
                                                    x_board_name=kwargs['x_board_name'],
                                                    x_percentage=kwargs['x_percentage'],
                                                    xii_year=kwargs['xii_year'],
                                                    xii_board_name=kwargs['xii_board_name'],
                                                    xii_percentage=kwargs['xii_percentage'], )
        userprofile.save()


class CompanyRegisterFormView(CreateView):
    model = CompanyProfile
    form_class = CompanyRegisterForm
    template_name = 'company/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()
        CompanyRegisterFormView.create_profile(user, **form.cleaned_data)
        return super(CompanyRegisterFormView, self).form_valid(form)

    @staticmethod
    def create_profile(user=None, **kwargs):
        # Creates a new UserProfile object after successful creation of User object
        userprofile = CompanyProfile.objects.create(user=user, name=kwargs['name'], domain=kwargs['domain'],
                                                    url=kwargs['url'], city=kwargs['city'], state=kwargs['state'],
                                                    country=kwargs['country'], pin_code=kwargs['pin_code'])
        userprofile.save()
