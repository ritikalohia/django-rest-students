from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('students/', views.getStudents),
    path('students/create/', views.createStudent),
    path('students/<str:pk>/update/', views.updateStudent),
    path('students/<str:pk>/delete/', views.deleteStudent),
    path('students/<str:pk>/', views.getStudent),
]
