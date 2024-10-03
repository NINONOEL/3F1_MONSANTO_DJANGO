from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_one_index'),
    path('about/', views.about, name='app_one_about'),
    path('contact/', views.contact, name='app_one_contact'),
]
