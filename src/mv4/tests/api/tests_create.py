import pytest
from typing import Union, Optional
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import tag
from django.urls import reverse
from rest_framework import status

from app.tests.api import APITestCase
from django.core import mail
from celery import shared_task

from mixer.backend.django import mixer, get_file
from django.test import TestCase
from django.test import TestCase, override_settings
from mock import mock
from mv4.models import MV4
pytestmark = [pytest.mark.django_db]


@pytest.fixture
def simple_mv4(mixer):
    return mixer.blend(MV4)


@pytest.fixture
def baseMV4URI():
    return reverse("file-list")

@pytest.fixture
def mv4_file():
    return SimpleUploadedFile("example.jpg", b"content", content_type="image/jpg")


def test_create_account(api, baseMV4URI, mv4_file):
    payload = {
        "file": mv4_file
    }
    data = api.post(baseMV4URI, payload, format='multipart')
    assert data['id']
    
def test_update_size(api, baseMV4URI, simple_mv4):
    payload = {
        "width": 14,
        "height": 12,
    }
    url = baseMV4URI + str(simple_mv4.id) + '/'
    data = api.patch(url, payload)
    assert data['success']
    



def test_get_mv4(api, baseMV4URI, simple_mv4):
    url = baseMV4URI + str(simple_mv4.id) + '/'
    data = api.get(url)

    assert data['id']
    assert isinstance(data['filename'], str)
    assert isinstance(data['processing'], bool)
    assert isinstance(data['processingSuccess'], Optional[bool])

import os
from os import path

MOCK_MP4_FILE = path.abspath(path.join(
    path.dirname(path.dirname(__file__)), 'resources', 'file.mp4'
))

from mv4.tasks import _change_video_resolution

@pytest.fixture
def mv4_with_file(mixer):
    file = get_file(MOCK_MP4_FILE)
    return mixer.blend(MV4, file=file)

def test_change_video_resolution(mv4_with_file):
    _change_video_resolution(mv4_with_file.pk, 100, 100)
    print(MV4.objects.get(pk=mv4_with_file.id).file.name)