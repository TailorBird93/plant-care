from django.urls import path
from . import views

urlpatterns = [
    path('', views.CareListView.as_view(), name='care-list'),
    path('create/', views.CareCreateView.as_view(), name='care-create'),
    path('<int:pk>/update/', views.CareUpdateView.as_view(), name='care-update'),
    path('<int:pk>/delete/', views.CareDeleteView.as_view(), name='care-delete'),
]
