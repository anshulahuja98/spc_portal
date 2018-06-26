from django.urls import path
from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html'), name ='home'),
    path('gradesystem/', TemplateView.as_view(template_name='main/gradesystem.html'), name='gradesystem'),
    path('programs/', TemplateView.as_view(template_name='main/programs.html')),
    path('rules/', TemplateView.as_view(template_name='main/rules.html')),
    path('placementProcedure/', TemplateView.as_view(template_name='main/placementprocedure.html')),
    path('newBreed/', TemplateView.as_view(template_name='main/newbreed.html')),
    path('coe/', TemplateView.as_view(template_name='main/coe.html')),
    path('research/', TemplateView.as_view(template_name='main/research.html')),
    path('facilities/', TemplateView.as_view(template_name='main/facilities.html')),
    path('contacts/', TemplateView.as_view(template_name='main/contacts.html')),

]
