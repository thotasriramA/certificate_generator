from . import views
from django.urls import path

urlpatterns = [

    # FIRST PAGE
    path('', views.index, name='index'),

    # AFTER LOGIN
    path('home/', views.home, name='home'),

    path('courses/', views.courses, name='courses'),
    path('languages/', views.languages, name='languages'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('about/', views.about, name='about'),

    path('signup/', views.signup, name='signup'),
    path('login_page/', views.login_page, name='login_page'),

    path('fullstackdevelopment/', views.fullstackdevelopment, name='fullstackdevelopment'),

    path('datanalysiscourse/', views.datanalysiscourse, name='datanalysiscourse'),

    path('chatbot/', views.chatbot, name='chatbot'),
    path('chatboat/', views.chatboat, name='chatboat'),
    path('logout/', views.logout_page, name='logout_page'),
    path('datasciencecourse/', views.datasciencecourse, name='datasciencecourse'),
    path('aiandmachinelearningcourse/', views.aiandmachinelearningcourse, name='aiandmachinelearningcourse'),
    path('pythonpdf/', views.pythonpdf, name='pythonpdf'),
    
]