from django.contrib import admin
from django.urls import path, include
from company import views
from accounts.views import CompanyRegisterView
from django.views.generic import TemplateView

urlpatterns = [

    path('register/', CompanyRegisterView.as_view()),
    # path('', TemplateView.as_view(template_name='company/base.html')),
    # path('home/',views.company_home),
    # path('addJobOffer/', views.addjoboffer),
    # path('addInternOffer/',views.addinternoffer),
    # path('logout/',views.logout)
]
