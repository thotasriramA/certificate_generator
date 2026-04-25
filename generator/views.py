from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
def signup(request):
    return render(request, 'signup.html')
def courses(request):
    return render(request, 'courses.html')
def login(request):
    return render(request, 'login.html')
def languages(request):
    return render(request, 'languages.html')

def roadmap(request):
    return render(request, 'roadmap.html')
def about(request):
    return render(request, 'about.html')

def fullstackdevelopment(request):
    return render(request, 'fullstackdevelopment.html')
    
