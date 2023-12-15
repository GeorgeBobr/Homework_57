from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import TaskForm
from webapp.models import Task


class TaskListView(TemplateView):
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        tasks = Task.objects.order_by("-updated_at")
        context = {"tasks": tasks}
        return context


class TaskCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        print(form)
        return render(request, "create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.get("type")

            task = Task.objects.create(
                summary=form.cleaned_data.get("summary"),
                description=form.cleaned_data.get("description"),
                status=form.cleaned_data.get("status")
            )
            if types:
                task.type.set(types)

            return redirect("task_list")
        else:
            print(form.errors)
            return render(request, "create.html", {"form": form})


def TaskUpdateView(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "GET":
        form = TaskForm(initial={
            "summary": task.summary,
            "description": task.description,
            "types": task.types.all(),
            "status": task.status
        })
        return render(request, "edit.html", {"form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.get("types")
            status = form.cleaned_data.get("status")
            task.summary = form.cleaned_data.get("summary")
            task.description = form.cleaned_data.get("description")
            task.types.set(types)
            task.status = status
            task.save()
            return redirect("task_list")
        else:
            return render(request, "edit.html", {"form": form})



def TaskDeleteView(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "GET":
        return render(request, "delete.html", {"task": task})
    else:
        task.delete()
        return redirect("task_list")


class TaskDetailView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, id=kwargs['id'])
        return context

    def get_template_names(self):
        return "detail.html"