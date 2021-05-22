from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from . import views

urlpatterns = [
    path("signup",views.signup,name="signup"),
    path("accounts",include('allauth.urls')),
    path("signin",views.signin,name="signin"),
    path("logout",views.logout,name="logout"),
]
