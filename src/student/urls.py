from django.urls import path
from .views import LoginView, DetailsView, JobOffersListView, InternOffersListView, ResumeUploadView
from django.contrib.auth.views import LogoutView

app_name = 'student'

urlpatterns = [
    path('login/', LoginView.as_view(), {'next_page': 'student:detail'}, name='login'),
    path('details/', DetailsView.as_view(), name="detail"),
    path('intern_offers/', InternOffersListView.as_view(), name='intern_offers'),
    path('intern_offers/', JobOffersListView.as_view(), name='job_offers'),
    path('resume_upload/', ResumeUploadView.as_view(), name='resume_upload'),
    path('logout/', LogoutView.as_view(next_page='main:home'), name='logout'),
]
