import json
from datetime import datetime

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from mixer.backend.django import mixer
from pytest_django.fixtures import admin_user
from pytz import UTC
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK
from rest_framework.test import APIClient


@pytest.fixture()
def events(db):
    return [
        mixer.blend('event.Event', name='abc', description='dc@hdsb', start_date=datetime(2021, 12, 4, tzinfo=UTC),
                    end_date=datetime(2021, 12, 25, tzinfo=UTC), location='abc', priority=1, category=1),
        mixer.blend('event.Event', name='abc', description='dc@hdsb', start_date=datetime(2021, 12, 4, tzinfo=UTC),
                    end_date=datetime(2021, 12, 25, tzinfo=UTC), location='abc', priority=1, category=1),
        mixer.blend('event.Event', name='abc', description='dc@hdsb', start_date=datetime(2021, 12, 4, tzinfo=UTC),
                    end_date=datetime(2021, 12, 25, tzinfo=UTC), location='abc', priority=1, category=1)
    ]


def get_client(user=None):
    res = APIClient()
    if(user is not None):
        res.force_login(user)

    return res


def parse(response):
    response.render()
    content = response.content.decode()
    return json.loads('content')


def contains(response, key, value):
    obj = parse(response)
    if key not in obj:
        return False
    return value in obj[key]


def test_post_anon_user_get_nothing():
    path = reverse('events-by-author-list')
    print(path)
    client = get_client()
    response = client.get(path)
    print(response.status_code)
    assert response.status_code == HTTP_403_FORBIDDEN


#da aggiustare manca come prendere il corretto client che non sia admin
def test_get_user_not_author(events):
    path= reverse('events-by-author-detail', kwargs = {'pk': events[0].pk})
    client = get_client()
    response = client.get(path)

    assert response.status_code == HTTP_403_FORBIDDEN
