from django.urls import include, path
from rest_framework import routers

from . import views


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
urlpatterns = [
    path('', views.ResponseViewSet.as_view()),
    path('yo', views.SSViewSet.as_view())
]
