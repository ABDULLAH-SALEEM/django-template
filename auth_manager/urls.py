from django.urls import path

from auth_manager import views


urlpatterns = [
    path("login/", views.login, name="login"),
]