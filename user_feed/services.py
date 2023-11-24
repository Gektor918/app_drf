from typing import Union

from django.db.models import QuerySet

from .models import *
from .serializers import *


def filter_note(user_id: str, search_query: str) -> Union[QuerySet, None]:
    """
    Filter notes based on user_id and search_query.
    """
    notes = Note.objects.filter(user = user_id, title__icontains=search_query).order_by('-created_at')
    
    if notes.exists():
        return notes


def filter_achievement(user_id: str) -> Union[QuerySet, None]:
    """
    Filter achievements based on user_id.
    """
    achievements = Achievement.objects.filter(id=user_id)

    if achievements.exists():
        return achievements


def filter_advertisements()-> QuerySet[Advertisement]:
    """
    Retrieve all advertisements ordered by published date.
    """
    advertisements = Advertisement.objects.all().order_by('-published_date')
    return advertisements