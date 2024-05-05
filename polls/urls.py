from django.urls import path

from polls import views

urlpatterns = [
    path("display_tasks/", views.display_tasks, name="display_tasks"),
    path("create_task/", views.create_task, name="create_task"),
    path("done/", views.done, name="done"),
    # path("delete_task/<str:name>/", views.delete_task, name="delete_task"),
]
