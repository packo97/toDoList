from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from event.models import Event
from event.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
