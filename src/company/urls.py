from django.urls import path
from django.views.generic import TemplateView

app_name = 'company'

urlpatterns = [
    path('dummy/', TemplateView.as_view(template_name="company/base.html"), name="dummy")
]
