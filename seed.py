import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_drf.settings')
django.setup()

from django.contrib.auth.models import User
from user_feed.models import UserProfile, Achievement

def create_users():
    for i in range(10):
        user = User.objects.create_user(f'user{i}', password='password')
        UserProfile.objects.create(user=user)

def create_achievements():
    for i in range(5):
        Achievement.objects.create(name=f'Achievement {i}', criteria='Criteria')

if __name__ == "__main__":
    create_users()
    create_achievements()