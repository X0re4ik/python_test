from rest_framework import viewsets


from mv4.api.serializers import \
    (MV4CreateSerializer,
     MV4PartialUpdateSerializer,
     MV4GetSerializer,
     MV4DeleteSerializer)
from mv4.models import MV4

class MV4ViewSet(viewsets.ModelViewSet):
    queryset = MV4.objects.all()
    serializer_class = MV4GetSerializer
    
    def get_serializer_class(self):
        if self.action == "create":
            return MV4CreateSerializer
        if self.action == "partial_update":
            return MV4PartialUpdateSerializer
        if self.action == "retrieve":
            return MV4GetSerializer
        if self.action == "destroy":
            return MV4DeleteSerializer
        return self.__class__.serializer_class
