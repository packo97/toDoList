import pytest
from django.core.exceptions import ValidationError
from mixer.backend.django import mixer


def test_more_than_50_characters_for_name(db):
    event = mixer.blend('event.Event',name='a'*51)
    with pytest.raises(ValidationError) as err:
        event.full_clean()


def test_check_only_characters_and_number_for_name(db):
    event = mixer.blend('event.Event', name='#dc@hdsb')
    with pytest.raises(ValidationError) as err:
        event.full_clean()


def test_more_than_500_characters_for_description(db):
    event = mixer.blend('event.Event', description='a' * 501)
    with pytest.raises(ValidationError) as err:
        event.full_clean()


def test_check_only_characters_and_number_for_description(db):
    event = mixer.blend('event.Event', description='dc@hdsb')
    with pytest.raises(ValidationError) as err:
        event.full_clean()

#problema
def test_startDate_is_after_current_date(db):
    event = mixer.blend('event.Event', start_date='2021-12-01 15:00:00')
    with pytest.raises(ValidationError) as err:
        event.full_clean()

#problema
def test_endtDate_is_after_current_date(db):
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

