from django.contrib import admin
from student.models import ProgramAndBranch


@admin.register(ProgramAndBranch)
class ProgramAndBranchAdmin(admin.ModelAdmin):
    class Meta:
        model = ProgramAndBranch
        fields = '__all__'

#
# @admin.register(Program)
# class ProgramAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Program
#         fields = '__all__'
