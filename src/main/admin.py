from django.contrib import admin
from .models import PastRecruiters, CoreTeamContacts, Volunteers, News, AlumniTestimonial, HomeImageCarousel, NavBarOptions, NavBarSubOptions
from import_export.admin import ImportExportActionModelAdmin


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


@admin.register(AlumniTestimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['ranking', 'alumni_name', 'active', ]
    list_filter = ['active', ]
    ordering = ['ranking', ]

    class Meta:
        model = AlumniTestimonial
        fields = '__all__'


@admin.register(HomeImageCarousel)
class HomeImageCarouselAdmin(admin.ModelAdmin):
    list_display = ['title', 'ordering', 'active', ]
    ordering = ['ordering', ]

    class Meta:
        model = HomeImageCarousel
        fields = '__all__'


@admin.register(NavBarOptions)
class NavBarOptionsAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    list_filter = ['active', ]
    search_fields = ['title', ]

    class Meta:
        model = NavBarOptions
        fields = '__all__'


@admin.register(NavBarSubOptions)
class NavBarSubOptionsAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    search_fields = ['title', ]

    class Meta:
        model = NavBarSubOptions
        fields = '__all__'
