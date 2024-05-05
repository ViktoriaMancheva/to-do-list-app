from django.forms import ModelForm
from .models import Task
from django import forms
from django.db import models


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


