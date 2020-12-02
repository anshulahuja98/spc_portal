from import_export import resources
from import_export.fields import Field
from .models import CompanyProfile, StudentProfile, CompanyPerson


class CompanyProfileResource(resources.ModelResource):
    country = Field(
        column_name='Country',
        attribute='get_country_display',
    )

    class Meta:
        model = CompanyProfile
        fields = ('name', 'domain', 'url', 'city', 'pin_code',)


class CompanyPersonResource(resources.ModelResource):
    company__country = Field(
        column_name='Country',
        attribute='get_country_display',
    )

    class Meta:
        model = CompanyPerson
        fields = (
            'company__country', 'company__name', 'company__domain', 'company__url', 'company__city',
            'company__pin_code', 'name', 'designation', 'phone', 'email', )
        export_order = (
            'company__country', 'company__name', 'company__domain', 'company__url', 'company__city',
            'company__pin_code', 'name', 'designation', 'email', 'phone',
        )


class StudentProfileResource(resources.ModelResource):
    nationality = Field(
        column_name='Nationality',
        attribute='get_nationality_display',
    )
    category = Field(
        column_name='Category',
        attribute='get_category_display')

    program_branch = Field(
        column_name='Program and Branch',
        attribute='program_branch__name')

    class Meta:
        model = StudentProfile
        fields = (
            'user__first_name', 'user__last_name', 'roll_no', 'user__email', 'year', 'gpa', 'ug_gpa', 'phone', 'dob',
            'jee_air', 'physical_disability', 'permanent_address', 'current_address', 'x_year',
            'x_board_name', 'x_percentage', 'xii_year', 'xii_board_name', 'xii_percentage', 'banned')
        export_order = (
            'user__first_name', 'user__last_name', 'roll_no', 'user__email', 'program_branch', 'year', 'gpa', 'ug_gpa', 'phone', 'dob',
            'jee_air', 'category', 'physical_disability', 'permanent_address', 'current_address', 'x_year',
            'x_board_name', 'x_percentage', 'xii_year', 'xii_board_name', 'xii_percentage', 'banned', 'nationality')
