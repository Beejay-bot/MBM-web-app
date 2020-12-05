from django.urls import path
from .views import *
app_name = 'info'

urlpatterns = [
    path("about-us/", AboutUsView, name="about-us"),
    path("contact-us/", ContactUsView.as_view(), name="contact-us")
]

