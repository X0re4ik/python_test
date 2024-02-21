

from mp4.models import MP4
from mp4.tasks import change_video_resolution

class MP4Maker:
    def __init__(self, file) -> None:
        self._file = file
        self._filename = file.name
    
    def create(self, *args, **kwargs):
        return MP4.objects.create(
            filename=self._filename,
            processing=True,
            file=self._file,  
        )
        
class MP4Updater:
    
    def __init__(self, instance) -> None:
        self._instance = instance
    
    def update_size(self, width, height):
        change_video_resolution.delay(self._instance.pk, width, height)
        return self._instance