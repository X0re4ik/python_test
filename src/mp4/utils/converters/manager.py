from celery import shared_task

from mp4.models import MP4
import ffmpeg
from django.core.files import File
from pathlib import Path
import random
import string

class FileConverterManager:
    
    def __init__(self, mp4: MP4) -> None:
        self._mp4 = mp4
        file: File = self._mp4.file    
        self._stream = ffmpeg.input(file.path)
        self._filename = self._get_new_file_path(file)
    
    @property
    def stream(self):
        return self._stream
    
    @stream.setter
    def stream(self, value):
        self._stream = value
    
    def _get_new_file_path(self, file: File):
        file_path = Path(file.path)
        file_name, file_extension = file_path.stem, file_path.suffix
        new_full_name = file_name + self._generate_random_suffix() + file_extension
        return file_path.parent / new_full_name

    def _generate_random_suffix(self, length=10):
        return ''.join(random.sample(string.ascii_lowercase, length))
    
    def save(self):
        self._stream = ffmpeg.output(self._stream, filename=self._filename)
        ffmpeg.run(self._stream, quiet=True)
        self._mp4.change_link_on_file(str(self._filename))