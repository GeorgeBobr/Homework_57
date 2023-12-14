from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<int:id>/', TaskDetailView.as_view(), name='detail'),
    path('task/create/', TaskCreateView.as_view(), name='create'),
    path('task/update/<int:id>/', TaskUpdateView, name='update'),
    path('task/delete/<int:id>/', TaskDeleteView, name='delete')
]