from django.urls import path
from .views import LoginView

app_name = 'company'

urlpatterns = [
    path('login/', LoginView.as_view(), {'next_page': ''}, name='login')
]
