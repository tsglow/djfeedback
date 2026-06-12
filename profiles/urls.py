from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view(), name="upload_profile"),
    path("list", views.ListProfile.as_view(), name="list_profile")
]

