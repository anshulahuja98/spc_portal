from import_export import resources
from import_export.fields import Field
from import_export.widgets import ManyToManyWidget
from company.models import JobOffer, InternshipOffer, JobAdvertisement, InternshipAdvertisement
from student.models import ProgramAndBranch


class BaseOfferResource(resources.ModelResource):
    company = Field(
        column_name='Company Name',
        attribute='company')
    designation = Field(
        column_name='Job/Intern Designation',
        attribute='profile__designation')
    roll_no = Field(
        column_name='Roll No',
        attribute='student__user__username')
    name = Field(
        column_name='Name',
        attribute='student__user__get_full_name')
    email = Field(
        column_name='Email ID',
        attribute='student__user__email')
    dob = Field(
        column_name='DOB(YYYY-MM-DD)',
        attribute='student__dob')
    year = Field(
        column_name='Current year of study',
        attribute='student__year')
    program_branch = Field(
        column_name='Program and Branch',
        attribute='student__program_branch__name')
    gpa = Field(
        column_name='GPA',
        attribute='student__gpa')
    phone = Field(
        column_name='Phone Number',
        attribute='student__phone')
    category = Field(
        column_name='Category',
        attribute='student__get_category_display')
    jee_air = Field(
        column_name='JEE AIR',
        attribute='student__jee_air')
    physical_disability = Field(
        column_name='Physical Disability',
        attribute='student__physical_disability')
    current_address = Field(
        column_name='Current Address',
        attribute='student__current_address')
    permanent_address = Field(
        column_name='Permanent Address',
        attribute='student__permanent_address')
    x_year = Field(
        column_name='Class X Year',
        attribute='student__x_year')
    x_board_name = Field(
        column_name='Class X Board',
        attribute='student__x_board_name')
    x_percentage = Field(
        column_name='Class X Percentage/CGPA',
        attribute='student__x_percentage')
    xii_year = Field(
        column_name='Class XII Year',
        attribute='student__xii_year')
    xii_board_name = Field(
        column_name='Class XII Board',
        attribute='student__xii_board_name')
    xii_percentage = Field(
        column_name='Class XII Percentage/CGPA',
        attribute='student__xii_percentage')
    nationality = Field(
        column_name='Nationality',
        attribute='student__get_nationality_display',
    )
    ctc = Field(
        column_name='CTC',
        attribute='profile__ctc')

    class Meta:
        abstract = True
        fields = ('company', 'is_accepted', 'ppo',)
        export_order = (
            'company', 'designation', 'roll_no', 'name', 'email', 'dob', 'year', 'program_branch', 'gpa', 'phone',
            'category',
            'jee_air', 'x_year', 'x_board_name', 'x_percentage', 'xii_year', 'xii_board_name', 'xii_percentage',
            'nationality', 'current_address', 'permanent_address', 'physical_disability', 'ctc')


class JobOfferResource(BaseOfferResource):
    class Meta:
        model = JobOffer


class InternshipOfferResource(BaseOfferResource):
    class Meta:
        model = InternshipOffer


class BaseAdvertisementResource(resources.ModelResource):
    eligible_program_branch = Field(attribute='eligible_program_branch',
                                    widget=ManyToManyWidget(ProgramAndBranch, field='name'))

    class Meta:
        abstract = True
        fields = (
            'company', 'designation', 'description', 'tentative_join_date', 'tentative_job_location',
            'ctc', 'gross_salary', 'bonus', 'bond', 'bond_details', 'resume_required',
            'resume_shortlist_criteria', 'aptitude_test_required', 'group_discussion_required',
            'number_of_technical_interviews', 'number_of_technical_tests', 'number_of_hr_rounds',
            'medical_test_required',
            'min_gpa', 'number_of_members', 'other_details',)

        export_order = (
            'company', 'designation', 'description', 'tentative_join_date', 'eligible_program_branch', 'min_gpa',
            'tentative_job_location', 'ctc', 'gross_salary', 'bonus', 'bond', 'bond_details', 'resume_required',
            'resume_shortlist_criteria', 'aptitude_test_required', 'group_discussion_required',
            'number_of_technical_interviews', 'number_of_technical_tests', 'number_of_hr_rounds',
            'medical_test_required',
            'number_of_members', 'other_details',)


class JobAdvertisementResource(BaseAdvertisementResource):
    class Meta:
        model = JobAdvertisement


class InternshipAdvertisementResource(BaseAdvertisementResource):
    class Meta:
        model = InternshipAdvertisement
