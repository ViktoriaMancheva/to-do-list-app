from django.urls import path

from polls import views

urlpatterns = [
    path("display_tasks/", views.display_tasks, name="display_tasks"),
    path("create_task/", views.create_task, name="create_task"),
    path("display_tasks/done/", views.done, name="done"),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
]