from django.contrib import admin
from .models import HomeImageCarousel


@admin.register(HomeImageCarousel)
class HomeImageCarouselAdmin(admin.ModelAdmin):
    list_display = ['title', 'ordering', 'active', ]

    class Meta:
        model = HomeImageCarousel
        fields = '__all__'
