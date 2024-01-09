from audioop import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, UpdateView, DeleteView, DetailView, CreateView
from django.urls import reverse_lazy
from webapp.forms import TaskForm
from webapp.models import Task, Project

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/create.html'
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.author = self.request.user
        task.save()
        return redirect('webapp:project_detail', pk=project.pk)

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.kwargs['pk']})

class TaskUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'tasks/update.html'
    model = Task
    form_class = TaskForm

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.project.pk})


class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    permission_required = 'webapp.delete_task'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().user

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.project.pk})


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.order_by('-created_at')
        return context