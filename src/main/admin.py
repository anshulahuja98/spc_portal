from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import News


@admin.register(News)
class NewsAdmin(ImportExportActionModelAdmin):
    list_display = ['title', 'active', 'order_no', 'document', 'content', 'link', ]
    list_filter = ['active', ]
    ordering = ['order_no']

    class Meta:
        model = News
        fields = '__all__'
