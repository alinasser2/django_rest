from django.urls import path
from . import views
from rest_framework_simplejwt.views import ( TokenObtainPairView , TokenRefreshView ) 
from  user.views import Login , Register

urlpatterns = [
    path("login/" , Login.as_view()),
    path("register/" , Register.as_view()),
    path ("api/token" , TokenObtainPairView.as_view()),
    path ("api/token/refresh" , TokenRefreshView.as_view())
]