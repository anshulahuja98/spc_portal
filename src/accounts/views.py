from django.contrib.auth.views import LoginView as DefaultLoginView
from django.shortcuts import reverse
from django.views.generic import CreateView
from .forms import StudentRegisterForm, CompanyRegisterForm
from accounts.models import StudentProfile, CompanyProfile
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
        elif self.request.user.is_staff:
            return url or '/admin'
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
        StudentProfile.student_register_email(StudentProfile.objects.get(user=user))
        return super(StudentRegisterFormView, self).form_valid(form)

    @staticmethod
    def create_profile(user=None, **kwargs):
        # Creates a new UserProfile object after successful creation of User object
        userprofile = StudentProfile.objects.create(user=user,
                                                    program_branch=kwargs['program_branch'],
                                                    year=kwargs['year'],
                                                    gpa=kwargs['gpa'],
                                                    ug_gpa=kwargs['ug_gpa'],
                                                    phone=kwargs['phone'],
                                                    dob=kwargs['dob'],
                                                    category=kwargs['category'],
                                                    jee_air=kwargs['jee_air'],
                                                    physical_disability=kwargs['physical_disability'],
                                                    nationality=kwargs['nationality'],
                                                    permanent_address=kwargs['permanent_address'],
                                                    current_address=kwargs['current_address'],
                                                    x_year=kwargs['x_year'],
                                                    x_board_name=kwargs['x_board_name'],
                                                    x_percentage=kwargs['x_percentage'],
                                                    xii_year=kwargs['xii_year'],
                                                    xii_board_name=kwargs['xii_board_name'],
                                                    xii_percentage=kwargs['xii_percentage'],
                                                    std_image=kwargs['std_image'])
        userprofile.save()


class CompanyRegisterFormView(CreateView):
    model = CompanyProfile
    form_class = CompanyRegisterForm
    template_name = 'company/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()
        CompanyRegisterFormView.create_profile(user, **form.cleaned_data)
        CompanyProfile.company_register_email(CompanyProfile.objects.get(user=user))
        CompanyProfile.company_details_email(CompanyProfile.objects.get(user=user))
        return super(CompanyRegisterFormView, self).form_valid(form)

    @staticmethod
    def create_profile(user=None, **kwargs):

        # Creates a new UserProfile object after successful creation of User object
        userprofile = CompanyProfile.objects.create(user=user, name=kwargs['name'], domain=kwargs['domain'],
                                                    url=kwargs['url'], city=kwargs['city'], state=kwargs['state'],
                                                    country=kwargs['country'], pin_code=kwargs['pin_code'],
                                                    contact=kwargs['contact'], )
        userprofile.save()
