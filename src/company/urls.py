from django.urls import path
from .views import LoginView
from django.views.generic import TemplateView
from .views import InternOfferFormView, JobOfferFormView
from django.contrib.auth.views import LogoutView

app_name = 'company'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('dummy/', TemplateView.as_view(template_name="company/base.html"), name="dummy"),
    path('joboffer_form/', JobOfferFormView.as_view(), name="job-offer-form"),
    path('internoffer_form/', InternOfferFormView.as_view(), name="intern-offer-form"),
    path('logout/', LogoutView.as_view(next_page='main:home'), name='logout')

]
