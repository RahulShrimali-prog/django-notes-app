from django.urls import path
from .templates.notes import views

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('create/', views.note_create, name='note_create'),
    path('update/<int:pk>/', views.note_update, name='note_update'),
    path('delete/<int:pk>/', views.note_delete, name='note_delete'),
]
