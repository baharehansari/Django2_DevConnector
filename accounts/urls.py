from django.urls import path
from . import views

urlpatterns = [
    path('add-education/', views.addEducation, name='add_education'),
    path('add-experience/', views.addExperience, name='add_experience'),
    path('create-profile/', views.createProfile, name='create_experience'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.loginPage, name='login'),
    path('profile/<int:pk>/', views.profilePage, name='profile'),
    path('profiles/', views.profilesPage, name='profiles'),
    path('register/', views.registerPage, name='register'),
]


