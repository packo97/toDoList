from datetime import datetime, tzinfo

from django.core.exceptions import ValidationError
from pytz import UTC


def validate_date(date_start: datetime) -> None:
    current_date = datetime.now()
    current_aware=datetime(current_date.year, current_date.month, current_date.day, current_date.hour, current_date.minute, current_date.second, current_date.microsecond, tzinfo=UTC)

    dt = (date_start - current_aware)
    #print(dt.days)
    if dt.days <0:
        raise ValidationError("start date is before of the current date")
