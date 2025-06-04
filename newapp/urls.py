from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path("addMedecin/", views.addMedecin, name="addMedecin"),
    path("delete/<int:id>",views.delete, name="delete"),
    path("modifier/<int:id>", views.modifier, name="modifier"),
    path('modifier/modifierMed/<int:id>', views.modifierMed, name="modifierMed"),
    
    
]