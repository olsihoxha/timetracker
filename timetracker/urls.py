
from django.contrib import admin
from django.urls import path
from user.urls import urlpatterns as auth_urls
from time_tracker.urls import urlpatterns as tracker_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += auth_urls
urlpatterns += tracker_urls
