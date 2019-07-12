from apps.carts.models import Cart, Advertise
from django.contrib.auth.models import User
from django.test import TestCase


class CartTestCase(TestCase):
    def setUp(self):
        u = User.objects.create(username='mehran', password='mehran1234')

    def test_cart(self):
        cart = Cart.objects.get(id=1)
        user = cart.user
        self.assertEqual(cart.__str__(), user.email+"'s card")
