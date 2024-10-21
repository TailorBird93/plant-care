from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlantListView.as_view(), name='plant-list'),
    path('<int:pk>/', views.PlantDetailView.as_view(), name='plant-detail'),
]
