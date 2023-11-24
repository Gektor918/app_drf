from django.urls import path

from user_feed.views import *

urlpatterns = [
    path('', FeedView.as_view()),
]