"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from todo_app.views import index, TagListView, TagCreateView, TaskCreateView, \
    TaskDeleteView, TaskUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("tags", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
]

app_name = "todo"
