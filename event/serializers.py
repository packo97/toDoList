from rest_framework import serializers

from event.models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('id','name','description','author','start_date','end_date','location')
        model = Event