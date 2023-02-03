from django.db import models

from user.models import User

TYPE = [('Manager', 'Manager'), ('Approver', 'Approver')]
TASK_STATUS = [('Approved', 'Approved'), ('Declined', 'Declined')]


class Client(models.Model):
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        db_table = 'clients'

    client_name = models.CharField('Client Name', max_length=200)


class ClientUsers(models.Model):
    class Meta:
        verbose_name = 'ClientUser'
        verbose_name_plural = 'ClientUsers'
        db_table = 'clientusers'

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_users')
    user_type = models.CharField(max_length=100, choices=TYPE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return f"{self.client.client_name}-{self.user.username}"


class Project(models.Model):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        db_table = 'projects'

    project_name = models.CharField('Name', max_length=50, unique=True)
    project_description = models.CharField('Description', max_length=512)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='client')

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
    status = models.CharField('Status', max_length=300, choices=TASK_STATUS)
    comments = models.CharField('Comments', max_length=300, null=True)

    def __str__(self):
        return self.task.task_code


class TimeTrackData(models.Model):
    class Meta:
        verbose_name = 'TimeTrackData'
        verbose_name_plural = 'TimeTrackData'
        db_table = 'time_track_data'

    comments = models.CharField('Comments', max_length=300, null=True)
    status = models.CharField('Status', max_length=300, choices=TASK_STATUS)
    client_user = models.ForeignKey(ClientUsers, on_delete=models.CASCADE, related_name='time_track_data')
    time_track = models.ForeignKey(TimeTrack, on_delete=models.CASCADE, related_name='time_track_data')
