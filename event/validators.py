from datetime import datetime

from django.core.exceptions import ValidationError


def validate_start_date(date_start: datetime) -> None:

    if(date_start == None):
        raise ValidationError("start date is null")

    current_date = datetime.now()
    difference = date_start - current_date
    seconds_in_day = 24 * 60 * 60
    result = divmod(difference.days * seconds_in_day + difference.seconds, 60)
    print(result[0])
    print(result[1])

    if(result[0] <= -5): #è possibile prenotare entro 5 minuti dall'inizio dell'evento
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

