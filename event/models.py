
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

from event.validators import validate_date


def priority_choices():
    choices = [(0,'ALTO'),(1,'MEDIO'),(2,'BASSO')]
    return choices


def category_choices():
    choices = [(0,'LAVORO'),(1,'SVAGO'),(2,'FAMIGLIA'),(3,'SCUOLA')]
    return choices


class Event(models.Model):

    name = models.CharField(max_length=50, validators=[RegexValidator(r'^[a-zA-Z0-9 ]+$')])

    description = models.CharField(max_length=500, validators=[RegexValidator(r'^[a-zA-Z0-9 ]+$')])

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    start_date = models.DateTimeField(validators=[validate_date])

    end_date = models.DateTimeField(validators=[validate_date])

    location = models.CharField(max_length=50, validators=[RegexValidator(r'^[a-zA-Z0-9 ]+$')])

    priority = models.IntegerField(choices=priority_choices())

    category = models.IntegerField(choices=category_choices())

    def clean(self, *args, **kwargs):
        print(self.start_date)
        if self.start_date is None or self.end_date is None:
            raise ValueError('start date or end date is Null')

        if self.start_date > self.end_date:
            raise ValueError('start date must be smaller or equals to end date')

    def save(self, *args, **kwargs):
        self.clean()
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


