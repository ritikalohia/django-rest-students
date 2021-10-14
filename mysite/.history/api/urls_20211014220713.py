from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getStudent),
    path('notes/create/', views.create),
    path('notes/<str:pk>/update/', views.updateNote),
    path('notes/<str:pk>/delete/', views.deleteNote),
    path('notes/<str:pk>/', views.getNote),
]
