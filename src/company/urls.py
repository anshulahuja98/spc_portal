from django.urls import path
from .views import LoginView
from django.views.generic import TemplateView

app_name = 'company'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('dummy/', TemplateView.as_view(template_name="company/base.html"), name="dummy")
]
