from django.urls import path, include
from .views import HomepageView, NavBarSubOptionsPageView

app_name = 'main'

urlpatterns = [
    path('', HomepageView.as_view(template_name='main/index.html'), name='home'),
    path('student/', include('student.urls')),
    path('company/', include('company.urls')),
    path('<slug:slug>', NavBarSubOptionsPageView.as_view(), name='navbarsuboptionpage')
]
