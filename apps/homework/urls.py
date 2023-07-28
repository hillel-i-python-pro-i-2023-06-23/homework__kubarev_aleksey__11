from django.urls import path
from . import views

app_name = 'homework'

urlpatterns = [
    path('generate-users/', views.users_generator_view, name='users_generator'),
]
