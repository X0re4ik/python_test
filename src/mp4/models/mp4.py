import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

class MP4(models.Model):
    id = models.UUIDField(
        _("Id"),
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    
    filename = models.CharField(
        _("Filename"), 
        max_length=50
    )

    processing = models.BooleanField(_("Processing"))
    
    processing_success = models.BooleanField(
        _("Processing success"),
        null=True, blank=True,
        default=None,
    )
    
    file = models.FileField(
        _("File"), 
        upload_to='mp4/',
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4'])
        ],
    )
    
    
    def change_link_on_file(self, path):
        self.file.storage.delete(self.file.name)
        self.file.name = path
        return self.save()