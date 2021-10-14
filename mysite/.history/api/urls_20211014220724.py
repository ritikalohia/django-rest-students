from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getStudent),
    path('notes/create/', views.createStudent),
    path('notes/<str:pk>/update/', views.updateStudent),
    path('notes/<str:pk>/delete/', views.deleteStudent),
    path('notes/<str:pk>/', views.getNote),
]
