from django.urls import path
from .views import *


urlpatterns = [
    path("", LandingPageView.as_view(), name="index")
]