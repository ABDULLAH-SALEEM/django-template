from django.urls import path
from auth_manager import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("auth-me/", views.auth_me, name="auth_me"),
]
