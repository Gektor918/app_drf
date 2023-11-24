from rest_framework import serializers
from user_feed.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'


class QuerySerializer(serializers.Serializer):
    user_id = serializers.IntegerField(
        required=True,
        help_text="User ID for filtering notes and achievements"
    )
    search = serializers.CharField(
        required=False,
        allow_blank=True,
        help_text="Search query for filtering notes by title"
    )