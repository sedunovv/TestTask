import pytest

from django.conf import settings
from rest_framework.test import APIClient


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '127.0.0.1',
        'NAME': 'interview_test',
    }


class Client(APIClient):
    pass


@pytest.fixture
def client():
    return Client()
