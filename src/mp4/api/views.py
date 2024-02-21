from rest_framework import viewsets


from mp4.api.serializers import \
    (MP4CreateSerializer,
     MP4PartialUpdateSerializer,
     MP4GetSerializer,
     MP4DeleteSerializer)
from mp4.models import MP4

class MP4ViewSet(viewsets.ModelViewSet):
    queryset = MP4.objects.all()
    serializer_class = MP4GetSerializer
    
    def get_serializer_class(self):
        if self.action == "create":
            return MP4CreateSerializer
        if self.action == "partial_update":
            return MP4PartialUpdateSerializer
        if self.action == "retrieve":
            return MP4GetSerializer
        if self.action == "destroy":
            return MP4DeleteSerializer
        return self.__class__.serializer_class
