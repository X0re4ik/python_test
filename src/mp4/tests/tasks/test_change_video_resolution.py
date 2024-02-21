import os
import pytest

from mixer.backend.django import mixer, get_file
from mp4.models import MP4
from mp4.tasks.change_video_resolution import _change_video_resolution, change_video_resolution


pytestmark = [pytest.mark.django_db]

MOCK_MP4_FILE = os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'resources', 'file.mp4'
))

@pytest.fixture
def mp4_with_file(mixer):
    file = get_file(MOCK_MP4_FILE)
    return mixer.blend(MP4, file=file)

@pytest.fixture
def mocked_change_video_resolution(mocker):  
    return mocker.patch("mp4.tasks.change_video_resolution.delay") 

def test_change_video_resolution(mp4_with_file):
    _change_video_resolution(mp4_with_file.pk, 100, 100)
    obj = MP4.objects.get(pk=mp4_with_file.id)
    assert obj.file.name
    assert not obj.processing
    assert obj.processing_success
    
def test_task_change_video_resolution(celery_app, mp4_with_file):
    change_video_resolution.delay((mp4_with_file.id), 120, 120).get()
    mp4 = MP4.objects.get(pk=mp4_with_file.id)
    assert mp4_with_file.file.name != mp4.file.name