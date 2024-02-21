from typing import Any
from celery import shared_task
from mp4.models import MP4
from mp4.utils.converters import FileConverterManager, ResolutionConverterOperation 


def _change_video_resolution(mp4_pk: Any, width: int, height: int):
    mp4 = MP4.objects.get(pk=mp4_pk)
    mp4.processing = True
    mp4.save()
    
    try:
        
        cm = FileConverterManager(mp4)
        cm.stream = ResolutionConverterOperation(cm.stream, width, height).run()
        cm.save()
        
    except:
        mp4.processing_success = False
    
    mp4.processing = False
    mp4.processing_success = True
    mp4.save()


@shared_task
def change_video_resolution(mp4_pk: Any, width, height):
    return _change_video_resolution(mp4_pk, width, height)