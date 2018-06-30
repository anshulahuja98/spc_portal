from django.urls import path
from .views import DetailsView, JobOffersListView, InternOffersListView, ResumeUploadView

app_name = 'student'

urlpatterns = [
    path('details/', DetailsView.as_view(), name="detail"),
    path('intern_offers/', InternOffersListView.as_view(), name='intern_offers'),
    path('intern_offers/', JobOffersListView.as_view(), name='job_offers'),
    path('resume_upload/', ResumeUploadView.as_view(), name='resume_upload'),
]
