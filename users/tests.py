from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="me",
            email="maim_me@gmail.com",
            password="pass123"
        )

        self.assertEquals(user.username, "me")
        self.assertEquals(user.email, "maim_me@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="admin",
            email="test@mail.ru",
            password="super123"
        )

        self.assertEquals(admin_user.username, "admin")
        self.assertEquals(admin_user.email, "test@mail.ru")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
