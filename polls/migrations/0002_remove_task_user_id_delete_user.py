# Generated by Django 5.0.4 on 2024-04-29 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]