from django.contrib import admin
from student.models import ProgramAndBranch, ProgramEmailId


@admin.register(ProgramAndBranch)
class ProgramAndBranchAdmin(admin.ModelAdmin):
    class Meta:
        model = ProgramAndBranch
        fields = '__all__'


@admin.register(ProgramEmailId)
class ProgramEmailIdAdmin(admin.ModelAdmin):
    list_display = ['email', 'program', 'year']

    class Meta:
        model = ProgramEmailId
        fields = '__all__'
