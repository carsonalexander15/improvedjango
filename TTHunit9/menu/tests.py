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


#Added the View tests for the elements that need work.
class MenuViewsTests(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(season='test')
        self.item = Item.objects.create(
            name='item',
            description='item description',
            chef=User.objects.create(username='test_user')
        )
        self.ingredient = Ingredient.objects.create(
            name='item ingredient'
        )

    def test_menu_detail_view(self):
        resp = self.client.get(reverse('menu_detail',
                                       kwargs={'pk': self.menu.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'test')
        self.assertTemplateUsed(resp, 'menu/menu_detail.html')

    def test_item_detail_view(self):
        resp = self.client.get(reverse('item_detail',
                                       kwargs={'pk': self.item.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/detail_item.html')

    def test_edit_menu_view(self):
        resp = self.client.get(reverse('menu_edit',
                                       kwargs={'pk': self.menu.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/menu_edit.html')