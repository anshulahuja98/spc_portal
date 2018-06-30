from django.contrib import admin
from .models import StudentProfile, CompanyPerson, CompanyProfile


class CompanyPersonInline(admin.StackedInline):
    model = CompanyPerson


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    # inlines = (ResumeInline,)

    class Meta:
        model = StudentProfile
        fields = '__all__'


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    inlines = (CompanyPersonInline,)

    class Meta:
        model = CompanyProfile
        fields = '__all__'
