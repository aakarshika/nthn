from .models import Response
from rest_framework import serializers


class ResponseSerializer(serializers.ModelSerializer):
    choice = QuestionSerializer(source='r_choice', read_only=True)
    user = UserSerializer(source='r_user', read_only=True)

    class Meta:
        model = Response
        fields = [
            'id',
            'r_description',
            'r_response_milliseconds',
        ]
