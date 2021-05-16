from django.shortcuts import render
from rest_framework import views
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse


class ResponseViewSet(views.APIView):
    """
    API endpoint that allows Responses to be viewed or edited.
    """

    def get(self, request, **kwargs):
        return Response("yoget", status=status.HTTP_200_OK)

    def post(self, request):
        return Response("yopost" + JSON.tostring(request), status=status.HTTP_200_OK)


class SSViewSet(View):
    def get(self, request, **kwargs):
        d = {'name': "Chutiya bhai"}

        return render(request, 'yo.html', d)
        # return HttpResponse(render)
