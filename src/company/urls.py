from django.urls import path
from django.views.generic import TemplateView
from .views import InternOfferFormView, JobOfferFormView, InternOffersAddedListView, JobOffersAddedListView

app_name = 'company'

urlpatterns = [

    path('intern_offers/', InternOffersAddedListView.as_view(), name='intern-offers-added'),
    path('job_offers/', JobOffersAddedListView.as_view(), name='job-offers-added'),
    path('dummy/', TemplateView.as_view(template_name="company/base.html"), name="dummy"),
    path('joboffer_form/', JobOfferFormView.as_view(), name="job-offer-form"),
    path('internoffer_form/', InternOfferFormView.as_view(), name="intern-offer-form"),

]
