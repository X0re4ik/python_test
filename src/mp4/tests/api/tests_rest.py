import pytest
from typing import Optional
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from mixer.backend.django import mixer, get_file
from mp4.models import MP4


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def simple_mp4(mixer):
    return mixer.blend(MP4)

@pytest.fixture
def baseMP4URI():
    return reverse("file-list")

@pytest.fixture
def mp4_file():
    return SimpleUploadedFile(
        "example.mp4", 
        b"content", 
        content_type="video/mp4"
    )


class TestAPIValidData:
    def test_create(self, api, baseMP4URI, mp4_file):
        payload = {
            "file": mp4_file
        }
        data = api.post(baseMP4URI, payload, format='multipart')
        
        assert data['id']

    def test_update_size(self, api, baseMP4URI, simple_mp4, mocked_change_video_resolution):
        payload = {
            "width": 26,
            "height": 28,
        }
        url = baseMP4URI + str(simple_mp4.id) + '/'
        data = api.patch(url, payload)
        
        assert data['success']
        mocked_change_video_resolution.assert_called_once_with(
            simple_mp4.id, 
            payload['width'], 
            payload['height']
        )

    def test_get(self, api, baseMP4URI, simple_mp4):
        url = baseMP4URI + str(simple_mp4.id) + '/'
        data = api.get(url)
        
        assert data['id']
        assert isinstance(data['filename'], str)
        assert isinstance(data['processing'], bool)
        assert isinstance(data['processingSuccess'], Optional[bool])

    def test_delete(self, api, baseMP4URI, simple_mp4):
        url = baseMP4URI + str(simple_mp4.id) + '/'
        data = api.delete(url)
        assert data == {}


class TestAPIUnValidData:
    def test_create_without_payload(self, api, baseMP4URI):
        payload = {}
        data = api.post(baseMP4URI, payload, format='multipart')
        assert data['error']
    
    def test_update_with_small_width(self, api, baseMP4URI, simple_mp4, mocked_change_video_resolution):
        payload = {
            "width": 12,
            "height": 28,
        }
        url = baseMP4URI + str(simple_mp4.id) + '/'
        data = api.patch(url, payload)
        
        assert data['error']
        assert mocked_change_video_resolution.assert_not_called