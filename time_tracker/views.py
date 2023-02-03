from datetime import datetime

from django.http import JsonResponse
from rest_framework.decorators import api_view

from time_tracker.models import TimeTrack
from time_tracker.serializers import TimeTrackSerializers, TimeTrackUpdateSerializers
from timetracker.common.api_views import TTrackerListCreateAPIView, TTrackerUpdateAPIView
from timetracker.common.tools import send_pdf_as_email


class TimeTrackerView(TTrackerListCreateAPIView):
    queryset = TimeTrack.objects.all()
    serializer_class = TimeTrackSerializers

    def get_queryset(self):
        user = self.request.user
        queryset = TimeTrack.objects.filter(user=user)
        return queryset


class TimeTrackerRetrieveUpdate(TTrackerUpdateAPIView):
    queryset = TimeTrack.objects.all()
    serializer_class = TimeTrackUpdateSerializers


@api_view(['POST'])
def generate_pdf_for_user(request):
    user = request.user
    if user.is_superuser:  # this condition is just for simplicity
        data = request.data
        employee = data['employee']
        date_string = data['date']
        date_object = datetime.strptime(date_string, "%Y-%m-%d").date()
        employee_data = TimeTrack.objects.filter(user_id=employee, working_date=date_object)
        if employee_data:
            send_pdf_as_email(employee_data, user.email)
            return JsonResponse({"ack": "Done"}, status=200)
        else:
            return JsonResponse({"error": "Name is not valid"}, status=400)
