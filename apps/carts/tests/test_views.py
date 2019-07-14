from django.test import TestCase
from apps.carts.models import *
from apps.carts.views import *


class CartViewsTestCase(TestCase):
    def setUp(self):
        u = User.objects.create(username='mehran', password='mehran1234')

    def test_cart(self):
        resp = self.client.get('/cart/1/')
        self.assertEqual(resp.status_code, 302)  # because it needs login
