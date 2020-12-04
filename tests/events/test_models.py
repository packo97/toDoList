import pytest
from django.core.exceptions import ValidationError
from mixer.backend.django import mixer
from datetime import datetime

from pytz import UTC


def test_more_than_50_characters_for_name(db):
    startdate = datetime(2021, 12, 4, tzinfo=UTC)
    enddate = datetime(2021, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event',name='a'*51, description='abc', start_date=startdate,
                        end_date=enddate, location='abc' , priority=1, category=1)
    with pytest.raises(ValidationError) as err:
        event.full_clean()
    #assert 'start date is before of the current date' in '\n'.join(err.value.messages)


def test_check_only_characters_and_number_for_name(db):
    startdate = datetime(2021, 12, 4, tzinfo=UTC)
    enddate = datetime(2021, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event', name='a#2/', description='abc', start_date=startdate,
                        end_date=enddate, location='abc', priority=1, category=1)
    with pytest.raises(ValidationError) as err:
        event.full_clean()
    #assert 'start date is before of the current date' in '\n'.join(err.value.messages)


def test_more_than_500_characters_for_description(db):
    startdate = datetime(2021, 12, 4, tzinfo=UTC)
    enddate = datetime(2021, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event', name='abc', description='a' * 501, start_date=startdate,
                        end_date=enddate, location='abc' , priority=1, category=1)
    with pytest.raises(ValidationError) as err:
        event.full_clean()
    #assert 'start date is before of the current date' in '\n'.join(err.value.messages)


def test_check_only_characters_and_number_for_description(db):
    startdate = datetime(2021, 12, 4, tzinfo=UTC)
    enddate = datetime(2021, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event',name='abc', description='dc@hdsb', start_date=startdate,
                        end_date=enddate, location='abc' , priority=1, category=1)
    with pytest.raises(ValidationError) as err:
        event.full_clean()
    #assert 'start date is before of the current date' in '\n'.join(err.value.messages)

def test_more_than_50_characters_for_location(db):
    startdate = datetime(2021, 12, 4, tzinfo=UTC)
    enddate = datetime(2021, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event', name='abc', description='dchdsb', start_date=startdate,
                        end_date=enddate, location='a'*51, priority=1, category=1)
    with pytest.raises(ValidationError) as err:
        event.full_clean()
    #assert 'start date is before of the current date' in '\n'.join(err.value.messages)

def test_check_only_characters_and_number_for_location(db):
    startdate = datetime(2021, 12, 4, tzinfo=UTC)
    enddate = datetime(2021, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event', name='abc', description='dchdsb', start_date=startdate,
                        end_date=enddate, location='a°,', priority=1, category=1)
    with pytest.raises(ValidationError) as err:
        event.full_clean()
    #assert 'start date is before of the current date' in '\n'.join(err.value.messages)


def test_null_startDate(db):
    enddate = datetime(2021, 12, 5, tzinfo=UTC)

    with pytest.raises(ValueError) as err:
        event = mixer.blend('event.Event', name='abc', description='dchdsb', start_date=None,
                            end_date=enddate, location='a', priority=1, category=1)
    assert 'start date or end date is Null' in str(err)


def test_startDate_is_before_current_date(db):
    startdate=datetime(2020, 12,3, tzinfo=UTC)
    enddate = datetime(2021, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event', name='provaname', description ='provadesc', start_date=startdate,
                        end_date=enddate, location='abc', priority=1, category=1)
    with pytest.raises(ValidationError) as err:
        event.full_clean()
    assert 'start date is before of the current date' in '\n'.join(err.value.messages)


def test_same_day_but_hour_after_start(db):
    startdate = datetime(2020, 12, 4, tzinfo=UTC)
    enddate = datetime(2020, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event',  name='provaname', description ='provadesc', start_date=startdate,
                        end_date=enddate, location='abc', priority=1, category=1)
    with pytest.raises(ValidationError) as err:
        event.full_clean()
    assert 'start date is before of the current date' in '\n'.join(err.value.messages)

def test_endDate_before_startDate(db):
    startdate = datetime(2020, 12, 10, tzinfo=UTC)
    enddate = datetime(2020, 12, 5, tzinfo=UTC)

    with pytest.raises(ValueError) as err:
        event = mixer.blend('event.Event', name='provaname', description ='provadesc', start_date=startdate, end_date=enddate, location='abc', priority=1, category=1)
        event.full_clean()


#test sul codice di priorità e categoria

def test_priority_value(db):
    startdate = datetime(2021, 12, 5, tzinfo=UTC)
    enddate = datetime(2021, 12, 25, tzinfo=UTC)

    event = mixer.blend('event.Event', name='provaname', description='provadesc', start_date=startdate,
                        end_date=enddate, location='abc', priority=5, category=1)
    with pytest.raises(ValidationError) as err:
        event.full_clean()

def test_category_value(db):
    startdate = datetime(2021, 12, 5, tzinfo=UTC)
    enddate = datetime(2021, 12, 25, tzinfo=UTC)

    event = mixer.blend('event.Event', name='provaname', description='provadesc', start_date=startdate,
                        end_date=enddate, location='abc', priority=1, category=8)
    with pytest.raises(ValidationError) as err:
        event.full_clean()


