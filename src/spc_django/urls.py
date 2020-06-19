"""spc_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from accounts.views import LoginView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

admin.site.site_title = 'SPC Administration'
admin.site.site_header = 'SPC Administration'
admin.site.index_title = 'Admin Panel'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('company/', include('company.urls')),
    path('student/', include('student.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='student/password_reset.html',
            html_email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/password_reset_subject.txt'),
        name='password_reset'),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(template_name='student/password_reset_done.html'),
        name='password_reset_done'),
    path(
        'reset/<uidb64>[0-9A-Za-z_-]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/',
        PasswordResetConfirmView.as_view(template_name='student/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(template_name='student/password_reset_complete.html'),
        name='password_reset_complete'),
    path('', include('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
