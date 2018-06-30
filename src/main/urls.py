from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html'), name='home'),
    path('gradesystem/', TemplateView.as_view(template_name='main/gradesystem.html'), name='gradesystem'),
    path('programs/', TemplateView.as_view(template_name='main/programs.html'), name='programs'),
    path('rules/', TemplateView.as_view(template_name='main/rules.html'), name='rules'),
    path('placementProcedure/', TemplateView.as_view(template_name='main/placementprocedure.html'),
         name='placementProcedure'),
    path('newBreed/', TemplateView.as_view(template_name='main/newbreed.html'), name='newBreed'),
    path('coe/', TemplateView.as_view(template_name='main/coe.html'), name='coe'),
    path('research/', TemplateView.as_view(template_name='main/research.html'), name='research'),
    path('facilities/', TemplateView.as_view(template_name='main/facilities.html'), name='facilities'),
    path('contacts/', TemplateView.as_view(template_name='main/contacts.html'), name='contacts'),
    path('admissions/', TemplateView.as_view(template_name='main/admissions.html'), name='admissions'),
    path('achievements/', TemplateView.as_view(template_name='main/achievements.html'), name='achievements'),
    path('profile/', TemplateView.as_view(template_name='main/prospective.html'), name='profile'),
    path('alumni/', TemplateView.as_view(template_name='main/alumni.html'), name='alumni'),
    path('student_rules/', TemplateView.as_view(template_name='main/student_rules.html'), name='student_rules'),
    path('internships/', TemplateView.as_view(template_name='main/internships.html'), name='internships'),
    path('brochure/', TemplateView.as_view(template_name='main/brochure.html'), name='brochure'),
    path('summary/', TemplateView.as_view(template_name='main/summary.html'), name='summary'),
    path('company_rules/', TemplateView.as_view(template_name='main/company_rules.html'), name='company_rules'),
    path('past_recruiters/', TemplateView.as_view(template_name='main/past_recruiters.html'), name='past_recruiters'),
    path('aipc/', TemplateView.as_view(template_name='main/aipc.html'), name='aipc'),
    path('jaf/', TemplateView.as_view(template_name='main/jaf.html'), name='jaf'),
    path('iaf/', TemplateView.as_view(template_name='main/iaf.html'), name='iaf'),
    path('reachus/', TemplateView.as_view(template_name='main/reachus.html'), name='reachus'),
    path('invitation/', TemplateView.as_view(template_name='main/invitation.html'), name='invitation'),
    path('dir_msg/', TemplateView.as_view(template_name='main/dir_msg.html'), name='dir_msg'),
    path('student/', include('student.urls')),
    path('company/', include('company.urls'))
    # path('accounts/',include('accounts.urls'))
]
