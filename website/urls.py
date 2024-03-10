from django.urls import path

from website.views import home, register_employee


urlpatterns = [
    path("", home, name="home"),
    path("register/", register_employee, name="register"),
]
