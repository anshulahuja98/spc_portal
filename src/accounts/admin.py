from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Resume, StudentProfile, CompanyPerson, CompanyProfile, CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _


class ResumeInline(admin.StackedInline):
    model = Resume


class CompanyPersonInline(admin.StackedInline):
    model = CompanyPerson


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    inlines = (ResumeInline,)

    class Meta:
        model = StudentProfile
        fields = '__all__'


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    inlines = (CompanyPersonInline,)

    class Meta:
        model = CompanyProfile
        fields = '__all__'


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
