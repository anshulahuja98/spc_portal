from django.urls import path
from .views import DetailsView, ResumeUploadView, InternshipOffersView, JobOffersView

app_name = 'student'

urlpatterns = [
    path('details/', DetailsView.as_view(), name="detail"),
    path('intern_offers/', InternshipOffersView.as_view(), name='intern-offers'),
    path('job_offers/', JobOffersView.as_view(), name='job-offers'),
    path('resume_upload/', ResumeUploadView.as_view(), name='resume_upload'),
]
