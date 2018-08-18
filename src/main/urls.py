from django.urls import path, include
from .views import HomepageView

app_name = 'main'

urlpatterns = [
    path('', HomepageView.as_view(template_name='main/index.html'), name='home'),
    path('gradesystem/', HomepageView.as_view(template_name='main/gradesystem.html'), name='gradesystem'),
    path('programs/', HomepageView.as_view(template_name='main/programs.html'), name='programs'),
    path('rules/', HomepageView.as_view(template_name='main/rules.html'), name='rules'),
    path('placementProcedure/', HomepageView.as_view(template_name='main/placementprocedure.html'),
         name='placementProcedure'),
    path('newBreed/', HomepageView.as_view(template_name='main/newbreed.html'), name='newBreed'),
    path('coe/', HomepageView.as_view(template_name='main/coe.html'), name='coe'),
    path('research/', HomepageView.as_view(template_name='main/research.html'), name='research'),
    path('facilities/', HomepageView.as_view(template_name='main/facilities.html'), name='facilities'),
    path('contacts/', HomepageView.as_view(template_name='main/contacts.html'), name='contacts'),
    path('admissions/', HomepageView.as_view(template_name='main/admissions.html'), name='admissions'),
    path('achievements/', HomepageView.as_view(template_name='main/achievements.html'), name='achievements'),
    path('profile/', HomepageView.as_view(template_name='main/prospective.html'), name='profile'),
    path('alumni/', HomepageView.as_view(template_name='main/alumni.html'), name='alumni'),
    path('student_rules/', HomepageView.as_view(template_name='main/student_rules.html'), name='student_rules'),
    path('internships/', HomepageView.as_view(template_name='main/internships.html'), name='internships'),
    path('brochure/', HomepageView.as_view(template_name='main/brochure.html'), name='brochure'),
    path('summary/', HomepageView.as_view(template_name='main/summary.html'), name='summary'),
    path('company_rules/', HomepageView.as_view(template_name='main/company_rules.html'), name='company_rules'),
    path('past_recruiters/', HomepageView.as_view(template_name='main/past_recruiters.html'), name='past_recruiters'),
    path('aipc/', HomepageView.as_view(template_name='main/aipc.html'), name='aipc'),
    path('jaf/', HomepageView.as_view(template_name='main/jaf.html'), name='jaf'),
    path('iaf/', HomepageView.as_view(template_name='main/iaf.html'), name='iaf'),
    path('reachus/', HomepageView.as_view(template_name='main/reachus.html'), name='reachus'),
    path('invitation/', HomepageView.as_view(template_name='main/invitation.html'), name='invitation'),
    path('dir_msg/', HomepageView.as_view(template_name='main/dir_msg.html'), name='dir_msg'),
    path('student/', include('student.urls')),
    path('company/', include('company.urls')),
    path('tutorial_student/', HomepageView.as_view(template_name='main/tutorial-student.html'), name='tutorial_student'),
    path('tutorial_company/', HomepageView.as_view(template_name='main/tutorial-company.html'), name='tutorial_company')
]
