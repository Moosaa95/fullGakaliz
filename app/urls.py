from django.urls import path
from .views import *


urlpatterns = [
    path("", LandingPageView.as_view(), name="index"),
    path("about", AboutPageView.as_view(), name="about"),
    path("contact", ContactPageView.as_view(), name="contact"),
    path("contact_form", ContactAPiView.as_view(), name="contact_form"),
]