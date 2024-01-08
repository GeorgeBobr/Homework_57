from django.urls import path
from .views.views import TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from .views.project_views import (ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView,
                                  ProjectDeleteView, ProjectUsersView)
app_name = 'webapp'
urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),

    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/task/create/', TaskCreateView.as_view(), name='create'),
    path('<int:pk>/users/', ProjectUsersView.as_view(), name='project_users'),

    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

    path('task/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='update'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='delete')
]