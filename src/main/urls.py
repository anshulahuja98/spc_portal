from django.urls import path, include
from .views import HomepageView, NavBarSubOptionsPageView

app_name = 'main'

urlpatterns = [
    path('', HomepageView.as_view(template_name='main/index.html'), name='home'),
    path('student/', include('student.urls')),
    path('company/', include('company.urls')),
    path('tutorial_student/', HomepageView.as_view(template_name='main/tutorial-student.html'),
         name='tutorial_student'),
    path('tutorial_company/', HomepageView.as_view(template_name='main/tutorial-company.html'), name='tutorial_company'),
    path('<slug:slug>/', NavBarSubOptionsPageView.as_view(), name='navbarsuboptionpage')
]
