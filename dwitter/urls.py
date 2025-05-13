from django.urls import path
from dwitter.views import dashboard, profile_list, profile,home

app_name = "dwitter"

urlpatterns = [
    path('', home, name="dashboard"),
    path('dashboard/', dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile")
]