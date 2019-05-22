from django.contrib.auth.views import LoginView as DefaultLoginView
from django.shortcuts import reverse
from django.views.generic import CreateView
from .forms import StudentRegisterForm, CompanyRegisterForm
from accounts.models import StudentProfile, CompanyProfile
from main.views import HomepageView
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string


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
                                                    xii_percentage=kwargs['xii_percentage'], )
        userprofile.save()

        # Sends email to the registered student
        subject = "Registered with SPC"
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email, ]
        with open(settings.BASE_DIR + "/templates/accounts/student_register_email.txt") as f:
            register_message = f.read()
        message = EmailMultiAlternatives(subject=subject, body=register_message, from_email=from_email, to=to_email)
        html_template = render_to_string("accounts/student_register_email.html", {'username': user.username, 'email': user.email})
        message.attach_alternative(html_template, "text/html")
        message.send()


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
                                                    country=kwargs['country'], pin_code=kwargs['pin_code'],
                                                    contact=kwargs['contact'],)
        userprofile.save()

        # Sends email to the registered company
        subject = "Registered with SPC"
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.username, ]
        with open(settings.BASE_DIR + "/templates/accounts/company_register_email.txt") as f:
            register_message = f.read()
        message = EmailMultiAlternatives(subject=subject, body=register_message, from_email=from_email, to=to_email)
        html_template = render_to_string("accounts/company_register_email.html", {'username': user.username})
        message.attach_alternative(html_template, "text/html")
        message.send()

        # Sends details of the registered company
        subject1 = "Company Registered with SPC"
        from_email1 = settings.EMAIL_HOST_USER
        to_email1 = [settings.TO_EMAIL, ]
        with open(settings.BASE_DIR + "/templates/accounts/company_details_email.txt") as f1:
            details_message = f1.read()
        message1 = EmailMultiAlternatives(subject=subject1, body=details_message, from_email=from_email1, to=to_email1)
        html_template1 = render_to_string("accounts/company_details_email.html", {'name': kwargs['name'], 'email': user.username,
                                                                                  'domain': kwargs['domain'], 'url': kwargs['url'],
                                                                                  'city': kwargs['city'], 'state': kwargs['state'],
                                                                                  'contact': kwargs['contact']})
        message1.attach_alternative(html_template1, "text/html")
        message1.send()
