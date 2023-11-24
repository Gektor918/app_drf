from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .services import *


class FeedView(APIView, PageNumberPagination):

    @swagger_auto_schema(
        query_serializer=QuerySerializer,
        responses={
            200: openapi.Response('Successful response containing notes, achievements, and advertisements'),
            400: openapi.Response('Bad Request - user_id is not provided or is an empty string'),
            404: openapi.Response('Not Found - No matching records found'),
        },
    )
    def get(self, request):
        """
        API view for retrieving a paginated feed of notes, achievements, and advertisements based on user_id and search_query.

        Parameters:
            - user_id (str): The user ID for filtering notes and achievements.
            - search_query (str): The search query for filtering notes by title.

        Returns:
            Response: Returns a paginated response containing notes, achievements, and advertisements serialized as JSON.
                    If no matching records are found, returns an error response with a 404 status code.
                    If user_id is not provided or is an empty string, returns an error response with a 400 status code.
        """
        user_id = request.query_params.get('user_id')
        search_query = request.query_params.get('search', '')

        if user_id is None or user_id == '':
            return Response({'error': 'user_id is not provided or is an empty string'}, status=status.HTTP_400_BAD_REQUEST)

        notes = filter_note(user_id, search_query)

        if notes is not None:

            page = self.paginate_queryset(notes, request, view=self)
            achievements = filter_achievement(user_id)
            advertisements = filter_advertisements()

            serializer = NoteSerializer(page, many=True)
            achievement_serializer = AchievementSerializer(achievements, many=True)
            advertisement_serializer = AdvertisementSerializer(advertisements, many=True)

            paginated_data = {
                'notes': serializer.data,
                'achievements': achievement_serializer.data,
                'advertisements': advertisement_serializer.data,
            }
            return self.get_paginated_response(paginated_data)

        return Response({'error': 'No matching records found'}, status=status.HTTP_404_NOT_FOUND)
