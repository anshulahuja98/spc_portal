from .models import NavBarOptions, PastRecruiters


def add_variable_to_context(request):
    return {
        'navbaroptions': NavBarOptions.objects.filter(active=True),
        'companies': PastRecruiters.objects.filter(active=True).order_by('company_order_no')
    }
