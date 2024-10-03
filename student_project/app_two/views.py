from django.shortcuts import render

def home(request):
    return render(request, 'app_two/home.html')

def services(request):
    return render(request, 'app_two/services.html')

def team(request):
    return render(request, 'app_two/team.html')
