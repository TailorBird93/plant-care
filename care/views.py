from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CareTask
from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
class CareListView(ListView):
    model = CareTask
    template_name = 'care/care_list.html'
    context_object_name = 'care_tasks'

    def get_queryset(self):
        return CareTask.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class CareCreateView(CreateView):
    model = CareTask
    fields = ['plant', 'task', 'frequency', 'next_due']
    template_name = 'care/care_form.html'
    success_url = reverse_lazy('care-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CareUpdateView(UpdateView):
    model = CareTask
    fields = ['plant', 'task', 'frequency', 'next_due', 'completed']
    template_name = 'care/care_form.html'
    success_url = reverse_lazy('care-list')

    def get_queryset(self):
        return CareTask.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class CareDeleteView(DeleteView):
    model = CareTask
    template_name = 'care/care_confirm_delete.html'
    success_url = reverse_lazy('care-list')

    def get_queryset(self):
        return CareTask.objects.filter(user=self.request.user)
