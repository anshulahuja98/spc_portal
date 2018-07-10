from django.urls import path
from .views import InternshipAdvertisementFormView, JobAdvertisementFormView, InternshipAdvertisementAddedListView, \
    JobAdvertisementsAddedListView, \
    OfferView

app_name = 'company'

urlpatterns = [
    path('intern_offers/', InternshipAdvertisementAddedListView.as_view(), name='intern-offers-added'),
    path('job_offers/', JobAdvertisementsAddedListView.as_view(), name='job-offers-added'),
    path('joboffer_form/', JobAdvertisementFormView.as_view(), name="job-offer-form"),
    path('internoffer_form/', InternshipAdvertisementFormView.as_view(), name="intern-offer-form"),
    path('offer/<uuid:id>/', OfferView.as_view(), name="offer")

]
