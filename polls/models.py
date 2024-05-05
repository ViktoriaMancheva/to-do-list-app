from django.db import models
from django import forms


class Task(models.Model):
    title = models.CharField(verbose_name="Заглавие", max_length=255)
    status = models.BooleanField(verbose_name="Статус", default=False)
    pub_date = models.DateField(verbose_name="Дата на публикуване")

    def __str__(self):
        return self.title


