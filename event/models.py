import string

from django.contrib.auth import get_user_model
from django.db import models


class Event(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=50)
    #priority = models.TextChoices('priority','ALTO MEDIO BASSO')
    #category = models.TextChoices('category','LAVORO FAMIGLIA SVAGO')

    def __str__(self):
        return self.name


