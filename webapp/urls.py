from django.urls import path
from .views.views import TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from .views.project_views import (ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView,
                                  ProjectDeleteView, ProjectUserAddView, ProjectUserRemoveView, ProjectUserView)
app_name = 'webapp'
urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),

    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/task/create/', TaskCreateView.as_view(), name='create'),

    path('<int:pk>/users/', ProjectUserView.as_view(), name='project_users'),
    path('<int:pk>/user/add/<int:user_pk>/', ProjectUserAddView.as_view(), name='project_user_add'),
    path('<int:pk>/user/remove/<int:user_pk>/', ProjectUserRemoveView.as_view(), name='project_user_remove'),

    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

    path('task/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='update'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='delete')
]