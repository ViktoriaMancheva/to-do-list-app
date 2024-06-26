from django.forms import ModelForm
from .models import Task


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class UpdateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status']
