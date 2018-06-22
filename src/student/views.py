from django.contrib.auth.views import LoginView as DefaultLoginView

class LoginView(DefaultLoginView):
    template_name = ''