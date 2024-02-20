import os
import pytest
from django.conf import settings
from mixer.backend.django import mixer as _mixer
from app.celery import app
from app.tests.api import APIClient

@pytest.fixture
def api():
    """ APIClient """
    return APIClient()


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': settings.CELERY_BROKER_URL,
        'result_backend': settings.CELERY_RESULT_BACKEND
    }
    
@pytest.fixture(scope='module')
def celery_app(request, celery_config):
    data = {
        **celery_config,
        'task_always_eager': True,
    }
    app.conf.update(**data)
    return app