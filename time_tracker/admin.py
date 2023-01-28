from django.contrib import admin

from time_tracker.models import Project, Task, TimeTrack

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TimeTrack)
