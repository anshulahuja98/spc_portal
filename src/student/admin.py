from django.contrib import admin
from student.models import Branch, Program


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    class Meta:
        model = Branch
        fields = '__all__'


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    class Meta:
        model = Program
        fields = '__all__'
