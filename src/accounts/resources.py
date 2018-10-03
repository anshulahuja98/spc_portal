from import_export import resources
from import_export.fields import Field
from .models import CompanyProfile, StudentProfile


class CompanyProfileResource(resources.ModelResource):
    country = Field(
        column_name='Country',
        attribute='get_country_display',
    )

    class Meta:
        model = CompanyProfile
        fields = ('name', 'domain', 'url', 'city', 'pin_code',)


