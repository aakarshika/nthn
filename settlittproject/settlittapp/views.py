from django.shortcuts import render
from .models import Voter, User, Photo, Question, QuestionSet, Response
from rest_framework import views
from .serializers import UserSerializer, VoterSerializer, PhotoSerializer, QuestionSerializer, QuestionSetSerializer, ResponseSerializer
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(views.APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, **kwargs):
        if kwargs.get("id", None):
            queryset = [User.objects.get(id=kwargs["id"])]
        else:
            queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        print("KWARGSSSSSSSSSSSSS",kwargs)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VoterViewSet(views.APIView):
    """
    API endpoint that allows Voters to be viewed or edited.
    """
    def get(self, request, **kwargs):
        if kwargs.get("id", None):
            queryset = [Voter.objects.get(id=kwargs["id"])]
        else:
            queryset = Voter.objects.all()
        serializer = VoterSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VoterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class PhotoViewSet(views.APIView):
    """
    API endpoint that allows Photos to be viewed or edited.
    """
    def get(self, request, **kwargs):
        if kwargs.get("id", None):
            queryset = [Photo.objects.get(id=kwargs["id"])]
        else:
            queryset = Photo.objects.all()
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class QuestionViewSet(views.APIView):
    """
    API endpoint that allows Questions to be viewed or edited.
    """
    def get(self, request, **kwargs):
        if kwargs.get("id", None):
            queryset = [Question.objects.get(id=kwargs["id"])]
        else:
            queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class QuestionSetViewSet(views.APIView):
    """
    API endpoint that allows QuestionSets to be viewed or edited.
    """
    def get(self, request, **kwargs):
        if kwargs.get("id", None):
            queryset = [QuestionSet.objects.get(id=kwargs["id"])]
        else:
            queryset = QuestionSet.objects.all()
        serializer = QuestionSetSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class ResponseViewSet(views.APIView):
    """
    API endpoint that allows Responses to be viewed or edited.
    """
    def get(self, request, **kwargs):
        if kwargs.get("id", None):
            queryset = [Response.objects.get(id=kwargs["id"])]
        else:
            queryset = Response.objects.all()
        serializer = ResponseSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




