from django import forms
from django.forms import DateTimeInput

from todo_app.models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class TaskForm(forms.ModelForm):
    dead_line_time = forms.DateTimeField(
        widget=DateTimeInput(
            format="%Y-%m-%d %H:%M:%S", attrs={"type": "datetime-local"}
        )
    )

    class Meta:
        model = Task
        fields = ["content", "dead_line_time", "tags"]
