from django.urls import path

from .views import UserListAPIView, UserCreateAPIView
urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/create/', UserCreateAPIView.as_view(), name='user-create'),
]
