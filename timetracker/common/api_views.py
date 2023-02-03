from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from timetracker.common.api_permissions import CanView, CanAdd, CanUpdate


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


class TTrackerUpdateAPIView(RetrieveUpdateAPIView):
    queryset = None
    serializer_class = None
    filter_serializer_class = None
    filter_map = {}
    queryset_kwargs = {}
    permission_classes = [CanView, CanUpdate]
