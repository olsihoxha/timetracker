from django.urls import path

from time_tracker.views import TimeTrackerView, generate_pdf_for_user, TimeTrackerRetrieveUpdate

urlpatterns = [
    path('time-tracks/', TimeTrackerView.as_view(), name='time-tracks'),
    path('get-employee-data/', generate_pdf_for_user, name='get-pdf-as-email'),
    path('give-feedback/<pk>/', TimeTrackerRetrieveUpdate.as_view(), name='give-feedback')
]
