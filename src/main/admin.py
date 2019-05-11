from django.contrib import admin
from .models import PastRecruiters, Contacts


@admin.register(PastRecruiters)
class PastRecruitersAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_order_no', 'active', ]
    list_filter = ['active', ]

    class Meta:
        model = PastRecruiters
        fields = '__all__'


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'active', ]
    list_filter = ['active', 'designation', ]
    ordering = ['order_no', ]

    class Meta:
        model = Contacts
        fields = '__all__'
