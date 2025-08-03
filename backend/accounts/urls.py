from django.urls import path

from .views import (CustomeTokenVerifyView, CustomeTokenRefreshView, CustomeTokenObtainPairView, LogOutView)

urlpatterns = [
    path('jwt/create/', CustomeTokenObtainPairView.as_view()),
    path('jwt/refresh/', CustomeTokenRefreshView.as_view()),
    path('jwt/verify/', CustomeTokenVerifyView.as_view()),
    path('logout/', LogOutView.as_view()),
]
