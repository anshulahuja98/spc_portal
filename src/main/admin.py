from django.contrib import admin
from .models import PastRecruiters, CoreTeamContacts, Volunteers


@admin.register(PastRecruiters)
class PastRecruitersAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_order_no', 'active', ]
    list_filter = ['active', ]

    class Meta:
        model = PastRecruiters
        fields = '__all__'


@admin.register(CoreTeamContacts)
class CoreTeamContactsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'designation', 'active', ]
    list_filter = ['active', 'designation', ]
    ordering = ['order_no', ]

    class Meta:
        model = CoreTeamContacts
        fields = '__all__'


@admin.register(Volunteers)
class VolunteersAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'active', ]
    list_filter = ['active', ]

    class Meta:
        model = Volunteers
        fields = '__all__'
