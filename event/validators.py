from datetime import datetime, tzinfo

from django.core.exceptions import ValidationError
from pytz import UTC


def validate_date(date_start: datetime) -> None:

    if(date_start == None):
        raise ValidationError("date is null")
    #datetime.now dà una data senza timezone, il mixer in automatico con il timezone
    current_date = datetime.now()
    current_aware=datetime(current_date.year, current_date.month, current_date.day, current_date.hour,
                   current_date.minute, current_date.second, current_date.microsecond, tzinfo=UTC)

    #current_date_trimmed=datetime(current_date.year, current_date.month, current_date.day)
    #print (current_date_trimmed)
    #date_start_trimmed=datetime(date_start.year, date_start.month, date_start.day)
    #print(date_start_trimmed)
    #dt=(date_start_trimmed - current_date_trimmed)

    dt = (date_start - current_aware)
    print(dt.days)
    if(dt.days <0 ):
        raise ValidationError("start date is before of the current date")

def validate_start_date():
    pass

def validate_end_date():
    pass