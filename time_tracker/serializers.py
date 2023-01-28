from django.db.transaction import atomic
from rest_framework import serializers

from time_tracker.models import TimeTrack
from timetracker.common.tools import check_time_overlap


class TimeTrackSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    task_code = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TimeTrack
        fields = ['id',
                  'working_date',
                  'time_start',
                  'time_end',
                  'task_description',
                  'task',
                  'task_code',
                  'user']
        extra_kwargs = {'id': {'read_only': True},
                        'task': {'write_only': True}}

    @atomic()
    def create(self, validated_data):
        data = validated_data
        if data['time_end'] < data['time_start']:
            raise serializers.ValidationError({"detail": "End time is greater than start time"})
        given_time = [data['time_start'], data['time_end']]
        user = self.context['request'].user
        check_time_overlap(TimeTrack, data['working_date'], given_time, user)
        data['user'] = user
        time_tracker = super(TimeTrackSerializers, self).create(data)
        return time_tracker

    @staticmethod
    def get_user(obj):
        return obj.user.email

    @staticmethod
    def get_task_code(obj):
        return obj.task.task_code
