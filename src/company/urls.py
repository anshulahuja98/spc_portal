from django.urls import path
from .views import InternshipAdvertisementFormView, JobAdvertisementFormView, InternshipAdvertisementAddedListView, \
    JobAdvertisementsAddedListView, \
    InternshipOfferView, JobOfferView

app_name = 'company'

urlpatterns = [
    path('intern_offers/', InternshipAdvertisementAddedListView.as_view(), name='intern-offers-added'),
    path('job_offers/', JobAdvertisementsAddedListView.as_view(), name='job-offers-added'),
    path('joboffer_form/', JobAdvertisementFormView.as_view(), name="job-offer-form"),
    path('internoffer_form/', InternshipAdvertisementFormView.as_view(), name="intern-offer-form"),
    path('internship_offer/<uuid:id>/', InternshipOfferView.as_view(), name="internship-offer"),
    path('job_offer/<uuid:id>/', JobOfferView.as_view(), name="job-offer")

]
