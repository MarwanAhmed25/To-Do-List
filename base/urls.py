from django.urls import path
from .views import tasks, task_detail, task_delete, task_update, task_create

urlpatterns = [
    path('', tasks, name='tasks'),
    path('task/<str:slug>/', task_detail, name='task'),
    path('task_delete/<str:slug>/', task_delete, name='task_delete'),
    path('task_update/<str:slug>/', task_update, name='task_update'),
    path('task_create/', task_create, name='task_create'),
]
