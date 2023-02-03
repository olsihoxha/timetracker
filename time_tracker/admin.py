from django.contrib import admin

from time_tracker.models import Project, Task, TimeTrack, TimeTrackData, ClientUsers, Client

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TimeTrack)
admin.site.register(TimeTrackData)
admin.site.register(ClientUsers)
admin.site.register(Client)
