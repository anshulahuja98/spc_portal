from django.test import SimpleTestCase, TestCase, Client
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from accounts.models import CompanyProfile
from django.contrib.auth.views import LogoutView


class TestAccountsUrlsResolves(SimpleTestCase):

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)


class TestAccountsUrlsResolves1(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.test_user = User.objects.create_user(username='testuser', password='AlphaBeta124')

    def test_login_redirects_to_supposed_url(self):
        self.company_test_user = CompanyProfile.objects.create(name='Test', user=self.test_user, domain='Consulting',
                                                               country='Indian', contact=1234567890)
        self.client.login(username='testuser', password='AlphaBeta124')
        response = self.client.get(reverse('login'), follow=True)
        self.assertRedirects(response, reverse('company:job-offers-added'))
