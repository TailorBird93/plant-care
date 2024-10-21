from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Plant
from .services import search_plants

class PlantListView(ListView):
    model = Plant
    template_name = 'plants/plant_list.html'
    context_object_name = 'plants'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return search_plants(query)
        return Plant.objects.all()

class PlantDetailView(DetailView):
    model = Plant
    template_name = 'plants/plant_detail.html'
    context_object_name = 'plant'
