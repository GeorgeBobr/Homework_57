from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.contrib.auth.models import User
from django.db.models import Q
from webapp.models import Project
from webapp.forms import ProjectForm, SimpleSearchForm
from django.views.generic import View, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model

class ProjectUserView(View):
    template_name = 'tracker/project_users.html'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        users = get_user_model().objects.exclude(projects=project)
        return render(request, self.template_name, {'project': project, 'users': users})

class ProjectUserAddView(View):
    def post(self, request, pk, user_pk):
        project = get_object_or_404(Project, pk=pk)
        user = get_object_or_404(get_user_model(), pk=user_pk)
        project.users.add(user)
        return redirect('webapp:project_users', pk=pk)

class ProjectUserRemoveView(View):
    def post(self, request, pk, user_pk):
        project = get_object_or_404(Project, pk=pk)
        user = get_object_or_404(get_user_model(), pk=user_pk)
        project.users.remove(user)
        return redirect('webapp:project_users', pk=pk)

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 5
    paginate_orphans = 3
    ordering = ('-start_date',)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Project.objects.all()

        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value) |
                Q(description__icontains=self.search_value)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = self.search_value
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = project.task_set.all()
        context['tasks'] = tasks
        return context

class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/project_create.html'
    form_class = ProjectForm
    model = Project

    def form_valid(self, form):
        self.project = form.save(commit=False)
        self.project.users = self.request.user
        self.project.save()
        form.save_m2m()
        return redirect('webapp:project_list', pk=self.project.pk)

class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    permission_required = 'webapp.edit_project'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().users

    def dispatch(self, request, *args, **kwargs):
        self.project = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Project, pk=self.kwargs.get('pk'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.project
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect('webapp:project_list')


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('webapp:project_list')

