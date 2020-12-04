from rest_framework import serializers
from rest_framework.exceptions import APIException

from event.models import Event, priority_choices, category_choices


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        'id', 'name', 'description', 'author', 'start_date', 'end_date', 'location', 'priority', 'priority_name','category', 'category_name',)
        model = Event

    priority_name = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data):
        if validated_data['author'] != self.context.get('request').user:
            raise APIException('exception author')
        return Event.objects.create(**validated_data)

    def get_author(self, instance):

        return self.context.get('request').user.id

    def get_priority_name(self, instance):
        choices = dict(priority_choices())
        return choices[instance.priority]

    category_name = serializers.SerializerMethodField(read_only=True)

    def get_category_name(self, instance):
        choices = dict(category_choices())
        return choices[instance.category]