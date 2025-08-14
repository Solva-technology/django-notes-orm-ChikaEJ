from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.all_notes, name='all_notes'),
    path('note_detail/<int:note_id>/', views.note_detail, name='note_detail'),
]
