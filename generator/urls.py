from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('languages/', views.languages, name='languages'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('about/', views.about, name='about'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('fullstackdevelopment/', views.fullstackdevelopment, name='fullstackdevelopment'),

]