from django.urls import path
from .views import InternOfferFormView, JobOfferFormView, InternProfilesAddedListView, JobProfilesAddedListView, \
    OfferView

app_name = 'company'

urlpatterns = [
    path('intern_offers/', InternProfilesAddedListView.as_view(), name='intern-offers-added'),
    path('job_offers/', JobProfilesAddedListView.as_view(), name='job-offers-added'),
    path('joboffer_form/', JobOfferFormView.as_view(), name="job-offer-form"),
    path('internoffer_form/', InternOfferFormView.as_view(), name="intern-offer-form"),
    path('offer/<uuid:id>/', OfferView.as_view(), name="offer")

]
