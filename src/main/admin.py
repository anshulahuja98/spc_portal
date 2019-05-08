from django.contrib import admin
from .models import nEws

class News(admin.ModelAdmin):
    list_display=('order_no','content','do_show','document')

admin.site.register(nEws,News)