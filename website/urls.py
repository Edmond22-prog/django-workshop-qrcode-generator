from django.urls import path

from website.views import generate_qrcode, home


urlpatterns = [
    path("", home, name="home"),
    path("generate_qrcode/", generate_qrcode, name="generate_qrcode"),
]
