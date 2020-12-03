from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, serializers
from rest_framework.permissions import IsAuthenticated

from event.models import Event, priority_choices
from event.permissions import IsAuthorOrReadOnly
from event.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    #permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventByAuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(author=self.request.user)
