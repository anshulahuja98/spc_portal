from django.contrib import admin
from django.urls import path, include
from accounts.views import StudentRegisterView

from student import views

urlpatterns = [
    path('register/', StudentRegisterView.as_view()),
    # path('login/', views.student=register),
    # path('home/',views.student_home),
    # path('uploadResume/',views.addResume),
    # path('editDetails/',views.editdetailsform),
    # path('viewOffers/',views.viewoffers)
    # path('logout/',views.logout)
]
