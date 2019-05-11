from django.contrib import admin
from .models import PastRecruiters
from .models import Testimonial
from import_export.admin import ImportExportActionModelAdmin

@admin.register(PastRecruiters)
class PastRecruitersAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_order_no', 'active', ]
    list_filter = ['active', ]

    class Meta:
        model = PastRecruiters
        fields = '__all__'


@admin.register(Testimonial)
class Testimonialsdmin(ImportExportActionModelAdmin):
    list_display = ['ranking', 'student_name', 'active', ]
    list_filter = ['active', ]
    ordering = ['ranking' ,]

    class Meta:
        model = Testimonial
