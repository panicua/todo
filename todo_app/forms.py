from django import forms

from todo_app.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
