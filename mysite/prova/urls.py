
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('aprovado/<int:matricula>/', views.aprovado, name = 'aprovado'),  
    path('info_disciplinas/<int:id>', views.info_disciplinas, name = 'info_disciplinas'),
]

