from django.db import models
from django import forms


class Task(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    pub_date = models.DateField()

    def __str__(self):
        return self.title
