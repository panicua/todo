from django.urls import path

from todo_app.views import (
    index,
    TagListView,
    TagCreateView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    change_task_status,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path(
        "task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "task/change_status/<int:pk>/",
        change_task_status,
        name="change-task-status",
    ),
]

app_name = "todo"
