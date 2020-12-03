import string

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

from event.validators import validate_start_date, validate_end_date


def priority_choices():
    choices = [(0,'ALTO'),(1,'MEDIO'),(2,'BASSO')]
    return choices



class Event(models.Model):

    #può contenere solo caratteri e numeri
    name = models.CharField(max_length=50, validators=[RegexValidator(r'^[a-zA-Z0-9]+$')])
    #può contenere solo caratteri e numeri
    description = models.CharField(max_length=500, validators=[RegexValidator(r'^[a-zA-Z0-9]+$')])
    #assegnazione automatica
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    #solo date future
    start_date = models.DateTimeField(validators=[validate_start_date])
    #non può essere prima della start date
    end_date = models.DateTimeField(validators=[validate_start_date])
    #può contenere solo caratteri e numeri
    location = models.CharField(max_length=50, validators=[RegexValidator(r'^[a-zA-Z0-9]+$')])

    priority = models.IntegerField(choices=priority_choices())

    category = models.IntegerField(choices=[(1,'LAVORO'),(2,'SVAGO'),(3,'FAMIGLIA'),(4,'SCUOLA')])


    def __str__(self):
        return self.name


