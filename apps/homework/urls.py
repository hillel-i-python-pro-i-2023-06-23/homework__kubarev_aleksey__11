from django.urls import path
from . import views

app_name = "homework"

urlpatterns = [
    path("generate-users/", views.generate_users, name="generate_users"),
    path("generate-users/<int:amount>/", views.generate_users, name="generate_users"),
]
