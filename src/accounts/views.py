from django.contrib.auth.views import LoginView as DefaultLoginView
from django.shortcuts import reverse


class LoginView(DefaultLoginView):
    template_name = 'main/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        url = super(LoginView, self).get_success_url()
        if hasattr(self.request.user, 'companyprofile'):
            return reverse('company:dummy')
        elif hasattr(self.request.user, 'studentprofile'):
            return reverse('student:detail')
        else:
            return url
