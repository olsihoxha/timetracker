from rest_framework.generics import ListAPIView, ListCreateAPIView

from timetracker.common.api_permissions import CanView, CanAdd


class TTrackerListAPIView(ListAPIView):
    queryset = None
    serializer_class = None
    filter_serializer_class = None
    filter_map = {}
    queryset_kwargs = {}
    permission_classes = [CanView]


class TTrackerListCreateAPIView(ListCreateAPIView):
    queryset = None
    serializer_class = None
    filter_serializer_class = None
    filter_map = {}
    queryset_kwargs = {}
    permission_classes = [CanView, CanAdd]
