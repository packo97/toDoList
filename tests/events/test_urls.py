import json
from datetime import datetime

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse
from mixer.backend.django import mixer
from pytest_django.fixtures import admin_user
from pytz import UTC
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED, \
    HTTP_500_INTERNAL_SERVER_ERROR
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
    if user is not None:
        res.force_login(user)

    return res


def parse(response):
    response.render()
    content = response.content.decode()
    return json.loads(content)


def test_post_anon_user_get_nothing():
    path = reverse('events-by-author-list')
    print(path)
    client = get_client()
    response = client.get(path)
    print(response.status_code)
    assert response.status_code == HTTP_403_FORBIDDEN


def test_get_user_not_author(events):
    path = reverse('events-by-author-detail', kwargs={'pk': events[0].pk})
    print(events[0].author)
    #print(path)
    client = get_client(User.objects.create_user('testUser','testUser@example.it', 'pwdtestUser')) #creazione user
    response = client.get(path)
    #print(response.status_code)
    assert response.status_code == HTTP_404_NOT_FOUND


def test_events_retrieve_a_single_event(events):
    path = reverse('events-by-author-detail', kwargs={'pk':events[0].pk})
    client = get_client(events[0].author)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert obj['name'] == events[0].name


def test_create_event_with_author_differente_from_me(events,admin_user):
    path = reverse('events-by-author-list')
    client = get_client(admin_user)

    startdate = datetime(2021, 12, 5, tzinfo=UTC)
    enddate = datetime(2021, 12, 25, tzinfo=UTC)
    response = client.post(path, data={'author':events[0].author.pk, 'name': 'Foo', 'description':'provadesc', 'start_date':startdate,
                        'end_date':enddate, 'location':'abc', 'priority':1, 'category':1})
    obj = parse(response)
    assert 'exception author' == obj['detail']


def test_create_event_with_author_equal_from_me(events):
    path = reverse('events-by-author-list')
    client = get_client(events[0].author)

    startdate = datetime(2021, 12, 5, tzinfo=UTC)
    enddate = datetime(2021, 12, 25, tzinfo=UTC)
    response = client.post(path, data={'author':events[0].author.pk, 'name': 'Foo', 'description':'provadesc', 'start_date':startdate,
                        'end_date':enddate, 'location':'abc', 'priority':1, 'category':1})
    assert response.status_code == HTTP_201_CREATED
