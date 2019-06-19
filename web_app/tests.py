from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.


class IndexPageTestCase(TestCase):

    """Test the index"""

    def test_index_page(self):
        response = self.client.get(reverse('web_app:index'))
        self.assertEqual(response.status_code, 200)


class RegisterPageTestCase(TestCase):

    """Test the register page"""

    def test_register_page(self):
        response = self.client.get(reverse('web_app:register'))
        self.assertEqual(response.status_code, 200)
