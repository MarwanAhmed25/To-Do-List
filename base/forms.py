from django.forms import ModelForm

from .models import Task


class ListForm(ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'title', 'description', 'complete']
