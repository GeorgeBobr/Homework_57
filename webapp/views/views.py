from audioop import reverse

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, UpdateView, DeleteView, DetailView, CreateView
from django.urls import reverse_lazy
from webapp.forms import TaskForm
from webapp.models import Task, Project

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/create.html'
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect('webapp:project_detail', pk=project.pk)

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.kwargs['pk']})

class TaskUpdateView(UpdateView):
    template_name = 'tasks/update.html'
    model = Task
    form_class = TaskForm
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('project_detail')

class TaskDetailView(TemplateView):
    model = Task
    template_name = 'tasks/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by('-created_at')
        return context