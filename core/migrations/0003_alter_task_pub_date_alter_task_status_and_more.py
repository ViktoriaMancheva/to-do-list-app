# Generated by Django 5.0.4 on 2024-04-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_task_user_id_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Дата на публикуване'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заглавие'),
        ),
    ]
