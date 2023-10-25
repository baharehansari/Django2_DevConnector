from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='index'),
    path('post/<slug:slug>/', views.postPage, name='post'),
    path('posts/', views.postsPage, name='posts'),
]
