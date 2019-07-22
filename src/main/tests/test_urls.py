from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import HomepageView


class TestMainUrlsResolve(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('main:home')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_gradesystem_url_resolve(self):
        url = reverse('main:gradesystem')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_programs_url_resolve(self):
        url = reverse('main:programs')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_rules_url_resolve(self):
        url = reverse('main:rules')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_placementProcedure_url_resolve(self):
        url = reverse('main:placementProcedure')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_contacts_url_resolve(self):
        url = reverse('main:contacts')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_admissions_url_resolve(self):
        url = reverse('main:admissions')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_achievements_url_resolve(self):
        url = reverse('main:achievements')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_profile_url_resolve(self):
        url = reverse('main:profile')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_alumni_url_resolve(self):
        url = reverse('main:alumni')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_student_rules_url_resolve(self):
        url = reverse('main:student_rules')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_internships_url_resolve(self):
        url = reverse('main:internships')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_why_recruit_url_resolve(self):
        url = reverse('main:why-recruit')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_brochure_url_resolve(self):
        url = reverse('main:brochure')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_summary_url_resolve(self):
        url = reverse('main:summary')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_company_rules_url_resolve(self):
        url = reverse('main:company_rules')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_past_recruiters_url_resolve(self):
        url = reverse('main:past_recruiters')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_aipc_url_resolve(self):
        url = reverse('main:aipc')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_jaf_url_resolve(self):
        url = reverse('main:jaf')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_iaf_url_resolve(self):
        url = reverse('main:iaf')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_reachus_url_resolve(self):
        url = reverse('main:reachus')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_invitation_url_resolve(self):
        url = reverse('main:invitation')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_dir_msg_url_resolve(self):
        url = reverse('main:dir_msg')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_tutorial_student_url_resolve(self):
        url = reverse('main:tutorial_student')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_tutorial_company_url_resolve(self):
        url = reverse('main:tutorial_company')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_chairman_msg_url_resolve(self):
        url = reverse('main:chairman_msg')
        self.assertEquals(resolve(url).func.view_class, HomepageView)
