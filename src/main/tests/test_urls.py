from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from main.views import HomepageView, NavBarSubOptionsPageView
from main.models import NavBarSubOptions, NavBarOptions


class TestMainUrlsResolve(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('main:home')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_tutorial_student_url_resolve(self):
        url = reverse('main:tutorial_student')
        self.assertEquals(resolve(url).func.view_class, HomepageView)

    def test_tutorial_company_url_resolve(self):
        url = reverse('main:tutorial_company')
        self.assertEquals(resolve(url).func.view_class, HomepageView)


class TestMainUrlsResolve1(TestCase):
    def setUp(self):
        self.test_nav_sub_option1 = NavBarSubOptions.objects.create(title='test-sub-nav-option1', description='description for test')
        self.test_nav_sub_option2 = NavBarSubOptions.objects.create(title='test-sub-nav-option2', use_custom_html=True,
                                                                    custom_html='main/achievements.html')
        self.test_nav_option = NavBarOptions.objects.create(title='test-nav-option')
        self.test_nav_option.sub_options.add(self.test_nav_sub_option1)
        self.test_nav_option.sub_options.add(self.test_nav_sub_option2)

    def test_slug_url_resolve(self):
        for sub_option in self.test_nav_option.sub_options.all():
            url = sub_option.get_absolute_url()
            self.assertEquals(resolve(url).func.view_class, NavBarSubOptionsPageView)
