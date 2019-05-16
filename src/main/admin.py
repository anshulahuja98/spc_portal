from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import News, PastRecruiters, HomeImageCarousel


@admin.register(News)
class NewsAdmin(ImportExportActionModelAdmin):
    list_display = ['order_no', 'title', 'active', ]
    list_filter = ['active', ]
    ordering = ['order_no']

    class Meta:
        model = News


@admin.register(PastRecruiters)
class PastRecruitersAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_order_no', 'active', ]
    list_filter = ['active', ]

    class Meta:
        model = PastRecruiters
        fields = '__all__'

@admin.register(HomeImageCarousel)
class HomeImageCarouselAdmin(admin.ModelAdmin):
    list_display = ['title', 'ordering', 'active', ]

    class Meta:
        model = HomeImageCarousel
        fields = '__all__'