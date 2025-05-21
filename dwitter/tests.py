from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Dweet


class ProfileModelTest(TestCase):
    def test_profile_created_on_user_creation(self):
        user = User.objects.create_user(username='testuser', password='pass123')
        self.assertTrue(Profile.objects.filter(user=user).exists())
        profile = Profile.objects.get(user=user)
        # A user should follow themselves after creation
        self.assertIn(profile, profile.follows.all())


class DweetModelTest(TestCase):
    def test_dweet_creation(self):
        user = User.objects.create_user(username='dweeter', password='pass123')
        dweet = Dweet.objects.create(user=user, body='This is my first dweet!')
        self.assertEqual(dweet.body, 'This is my first dweet!')
        self.assertEqual(dweet.user.username, 'dweeter')
        self.assertIsNotNone(dweet.created_at)