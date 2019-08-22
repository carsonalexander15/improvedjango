from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Menu, Item, Ingredient
from .forms import MenuForm


class MenuModelTests(TestCase):
    def test_create_menu_model(self):
        self.menu = Menu.objects.create(season='test')
        self.assertEqual(str(self.menu), self.menu.season)


class ItemModelTests(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            id='1',
            username='Test',
            email='test@test.com',
            password='test123'
        )

    def test_create_item_model(self):
        self.item = Item.objects.create(
            name='item',
            description='item description',
            chef=self.test_user
        )
        self.assertEqual(str(self.item), self.item.name)

