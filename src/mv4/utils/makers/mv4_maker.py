

from mv4.models import MV4


class MV4Maker:
    def __init__(self, file) -> None:
        self._file = file
        self._filename = file.name
    
    def create(self, *args, **kwargs):
        return MV4.objects.create(
            filename=self._filename,
            processing=True,
            file=self._file,  
        )
        
class MV4Updater:
    
    def __init__(self, instance) -> None:
        self._instance = instance
    
    def update_size(self, width, height):
        return self._instance