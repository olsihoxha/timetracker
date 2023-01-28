from django.db import models

from user.models import User


class Project(models.Model):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        db_table = 'projects'

    project_name = models.CharField('Name', max_length=50, unique=True)
    project_description = models.CharField('Description', max_length=512)

    def __str__(self):
        return self.project_name


class Task(models.Model):
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        db_table = 'tasks'

    task_code = models.CharField('Code', max_length=50, unique=True)  # assuming we have a jira ticket for the task
    task_name = models.CharField('Name', max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.task_code


class TimeTrack(models.Model):
    class Meta:
        verbose_name = 'TimeTrack'
        verbose_name_plural = 'TimeTracks'
        db_table = 'time_tracs'

    working_date = models.DateField("Working Date")
    task_description = models.CharField('Description', max_length=512)
    time_start = models.TimeField()
    time_end = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='time_tracks')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='time_tracks')
