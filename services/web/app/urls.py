from django.urls import path
from . import views
from .views import CEActionRequest


urlpatterns = [
    path("", views.index, name="index"),
    # path("CEAction/", CEActionRequest.select_municipality)
    path("CEAction/", CEActionRequest.select_municipality)
]
