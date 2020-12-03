import pytest
from django.core.exceptions import ValidationError
from mixer.backend.django import mixer
from datetime import datetime

from pytz import UTC


def test_more_than_50_characters_for_name(db):
    startdate = datetime(2020, 12, 4, tzinfo=UTC)
    enddate = datetime(2020, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event',name='a'*51, descrizione='abc', start_date=startdate, end_date=enddate, location='abc' )
    with pytest.raises(ValidationError) as err:
        event.full_clean()


def test_check_only_characters_and_number_for_name(db):
    startdate = datetime(2020, 12, 4, tzinfo=UTC)
    enddate = datetime(2020, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event', name='a#2/', descrizione='abc', start_date=startdate, end_date=enddate, location='abc')
    with pytest.raises(ValidationError) as err:
        event.full_clean()


def test_more_than_500_characters_for_description(db):
    startdate = datetime(2020, 12, 4, tzinfo=UTC)
    enddate = datetime(2020, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event', name='abc', description='a' * 501, start_date=startdate, end_date=enddate, location='abc')
    with pytest.raises(ValidationError) as err:
        event.full_clean()


def test_check_only_characters_and_number_for_description(db):
    startdate = datetime(2020, 12, 4, tzinfo=UTC)
    enddate = datetime(2020, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event',name='abc', description='dc@hdsb', start_date=startdate, end_date=enddate, location='abc')
    with pytest.raises(ValidationError) as err:
        event.full_clean()
    assert 'start date is before of the current date' in '\n'.join(err.value.messages)

#problema
def test_startDate_is_before_current_date(db):
    startdate=datetime(2020, 12,4, tzinfo=UTC)
    enddate = datetime(2020, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event', name='provaname', description ='provadesc', start_date=startdate, end_date=enddate, location='abc')
    with pytest.raises(ValidationError) as err:
        event.full_clean()
    #assert 'start date is before of the current date' in '\n'.join(err.value.messages)

#problema
def test_same_day_but_hour_after_start(db):
    startdate = datetime(2020, 12, 4, tzinfo=UTC)
    enddate = datetime(2020, 12, 5, tzinfo=UTC)
    event = mixer.blend('event.Event',  name='provaname', description ='provadesc', start_date=startdate, end_date=enddate, location='abc')
    with pytest.raises(ValidationError) as err:
        event.full_clean()


#problema
def test_endDate_before_startDate(db):
    event = mixer.blend('event.Event', start_date='2020-12-02 15:00:00', end_date='2020-12-01 15:00:00')
    with pytest.raises(ValidationError) as err:
        event.full_clean()

def test_more_than_50_characters_for_location(db):
    event = mixer.blend('event.Event',location='a'*51)
    with pytest.raises(ValidationError) as err:
        event.full_clean()

def test_check_only_characters_and_number_for_location(db):
    event = mixer.blend('event.Event', location='#dc@hdsb')
    with pytest.raises(ValidationError) as err:
        event.full_clean()

