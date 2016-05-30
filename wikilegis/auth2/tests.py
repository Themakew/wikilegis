from django.test import TestCase
from django.test.client import Client
from model_mommy import mommy
from wikilegis.auth2.models import User
from wikilegis.auth2.models import UserManager


class TestLogin(TestCase):

    def test_is_account_login_page(self):
        client = Client()
        response = client.get('/accounts/login/')
        self.failUnlessEqual(response.status_code, 200)


class TestModels(TestCase):

    def setUp(self):
        self.user = mommy.make(User)
        self.user_manager = UserManager()

    def test_get_full_name_when_the_full_name_is_informed(self):
        self.user.first_name = "First"
        self.user.last_name = "Last"
        self.assertEqual(self.user.get_full_name(), "First Last")

    def test_get_full_name_when_the_first_name_is_informed_empty(self):
        self.user.first_name = ""
        self.user.last_name = "Last"
        self.assertEqual(self.user.get_full_name(), "Last")

    def test_get_full_name_when_the_last_name_is_informed_empty(self):
        self.user.first_name = "First"
        self.user.last_name = ""
        self.assertEqual(self.user.get_full_name(), "First")

    def test_get_short_name_when_is_informed_the_first_name(self):
        self.user.first_name = "First"
        self.assertEqual(self.user.get_short_name(), "First")

    def test_get_display_name_when_is_informed_the_email(self):
        self.user.email = "test@test.com"
        self.assertEqual(self.user.get_display_name(), "test@test.com")

    def test_get_display_name_when_is_not_informed_the_email(self):
        self.user.email = ""
        self.assertEqual(self.user.get_display_name(), "")

    def test_get_display_name_when_is_informed_the_full_name(self):
        self.user.first_name = "First"
        self.user.last_name = "Last"
        self.user.get_full_name()
        self.assertEqual(self.user.get_display_name(), "First Last")

    def test_unicode_when_is_informed_the_display_name(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.__unicode__(), self.user.email)

    def test_get_absolute_url_when_email_is_not_informed(self):
        with self.assertRaises(ValueError) as context:
            self.user_manager._create_user("", 12345, False, False)
        self.assertTrue('The given email must be set' in context.exception)
