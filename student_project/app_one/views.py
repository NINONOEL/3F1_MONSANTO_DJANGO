from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'app_one/index.html')

def about(request):
    return render(request, 'app_one/about.html')

def contact(request):
    return render(request, 'app_one/contact.html')
