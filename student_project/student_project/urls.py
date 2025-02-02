"""
URL configuration for student_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_one import views as app_one_views  # Import the home view from app_one

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_one_views.home, name='home'),  # Add this line for the root URL
    path('app_one/', include('app_one.urls')),
    path('app_two/', include('app_two.urls')),
]

