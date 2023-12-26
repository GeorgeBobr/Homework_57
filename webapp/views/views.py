from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from webapp.forms import TaskForm
from webapp.models import Task, Project


class TaskCreateView(View):
    template_name = 'tasks/create.html'

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            project_pk = kwargs.get('pk')
            task = Task.objects.create(
                summary=form.cleaned_data.get("summary"),
                description=form.cleaned_data.get("description"),
                status=form.cleaned_data.get("status")
            )
            project = Project.objects.get(pk=project_pk)
            project.task_set.add(task)

            types = form.cleaned_data.get("type")
            if types:
                task.type.set(types)
            return redirect("webapp:project_detail", pk=project_pk)
        else:
            print(form.errors)
            return render(request, self.template_name, {"form": form})


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