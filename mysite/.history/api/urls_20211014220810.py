from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('students/', views.getStudent),
    path('notes/create/', views.createStudent),
    path('notes/<str:pk>/update/', views.updateStudent),
    path('notes/<str:pk>/delete/', views.deleteStudent),
    path('notes/<str:pk>/', views.getNote),
]