from django.urls import include, path
from rest_framework import routers

from . import views


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
urlpatterns = [	
	path('', views.UserViewSet.as_view()),
	path('user/', views.UserViewSet.as_view()),
	path('voter/', views.VoterViewSet.as_view()),
	path('photo/', views.PhotoViewSet.as_view()),
	path('question/', views.QuestionViewSet.as_view()),
	path('question-set/', views.QuestionSetViewSet.as_view()),
	path('response/', views.ResponseViewSet.as_view()),
	path('<int:id>/user/', views.UserViewSet.as_view()),
	path('<int:id>/voter/', views.VoterViewSet.as_view()),
	path('<int:id>/photo/', views.PhotoViewSet.as_view()),
	path('<int:id>/question/', views.QuestionViewSet.as_view()),
	path('<int:id>/question-set/', views.QuestionSetViewSet.as_view()),
	path('<int:id>/response/', views.ResponseViewSet.as_view()),
]