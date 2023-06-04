from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Yakisoba", price=50, inventory=100)

    def test_getall(self):
        response = self.client.get(reverse('menu_item_list'))
        item = Menu.objects.all()
        serializer = MenuSerializer(item, many=True)

        self.assertEqual(response.data, serializer.data)
