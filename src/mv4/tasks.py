

from celery import shared_task


from mv4.models import MV4
from typing import Any
import ffmpeg
from django.core.files import File
from pathlib import Path

        

def _change_video_resolution(mv4_pk: Any, width: int, height: int):
    mv4 = MV4.objects.get(pk=mv4_pk)
    file: File = mv4.file
    file_path = Path(file.path)
    
    file_name, suffix = file_path.stem, file_path.suffix
    new_full_name = file_name + "132748234" + suffix 
    new_name = file_path.parent / new_full_name
    
    stream = ffmpeg.input(file.path).filter('scale', w=width, h=height)
    stream = ffmpeg.output(stream, filename=new_name)
    ffmpeg.run(stream, quiet=True)
    
    mv4.change_file(str(new_name))

@shared_task
def change_video_resolution(mv4_pk: Any, width, height):
    return _change_video_resolution(mv4_pk, width, height)