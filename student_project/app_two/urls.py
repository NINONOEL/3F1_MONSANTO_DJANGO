from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app_two_home'),
    path('services/', views.services, name='app_two_services'),
    path('team/', views.team, name='app_two_team'),
]
    