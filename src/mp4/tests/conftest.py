import pytest

@pytest.fixture
def mocked_change_video_resolution(mocker):  
    return mocker.patch("mp4.tasks.change_video_resolution.delay") 