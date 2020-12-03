from datetime import datetime

from django.core.exceptions import ValidationError


def validate_start_date(date_start: datetime) -> None:

    if(date_start == None):
        raise ValidationError("start date is null")
    #datetime.now dà una data senza timezone, il mixer in automatico con il timezone
    current_date = datetime.now()
    current_date_trimmed=datetime(current_date.year, current_date.month, current_date.day)
    print (current_date_trimmed)
    date_start_trimmed=datetime(date_start.year, date_start.month, date_start.day)
    print(date_start_trimmed)
    dt=(date_start_trimmed - current_date_trimmed)

    print(dt.days)
    if(dt.days <0 ):
        raise ValidationError("start date is before of the current date")


def validate_end_date(date_end: datetime, date_start: datetime) -> None:

    if(date_end == None):
        raise ValidationError("end date is null")

    difference = date_end - date_start
    seconds_in_day = 24 * 60 * 60
    result = divmod(difference.days * seconds_in_day + difference.seconds, 60)
    print(result[0])
    print(result[1])

    if(result[0] <= 0): #non è possibile che la data di fine sia prima o uguale a quella di inizio
        raise ValidationError("start date is before of the current date")

