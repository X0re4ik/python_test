

from mp4.models import MP4
from rest_framework import serializers
from mp4.utils.makers import MP4Creator, MP4Updater


class toRepresentationMixin:
    def to_representation(self, instance):
        return {
            "success": True
        }

class _MP4Serializer(serializers.ModelSerializer):
    class Meta:
        model = MP4
        
    

class MP4CreateSerializer(_MP4Serializer):
    file = serializers.FileField(write_only=True) 
    class Meta(_MP4Serializer.Meta):
        fields = [
            'id',
            'file',    
        ]
    
    def create(self, validated_data):
        return MP4Creator(**validated_data).create()

class ResolutionField(serializers.Field):
    
    default_error_messages = {
        'incorrect_type': 'Incorrect type. Expected a integer, but got {input_type}',
        'out_of_range': 'Value out of range. Must be between 20 and +infinity.',
        'odd_number': 'The number must be even'
    }
    
    LOW_LIMIT_VALUE = 20
    
    def to_internal_value(self, data):
        
        if not isinstance(data, int):
            self.fail('incorrect_type', input_type=type(data).__name__)
        if data <= self.LOW_LIMIT_VALUE:
            self.fail('out_of_range', input_type=type(data).__name__)
        if data % 2 != 0:
            self.fail('odd_number')
        
        return data

class MP4PartialUpdateSerializer(toRepresentationMixin, _MP4Serializer):
    
    width = ResolutionField(write_only=True)
    height = ResolutionField(write_only=True)
    
    class Meta(_MP4Serializer.Meta):
        fields = [
            'width',
            'height', 
        ]
    
    def update(self, instance, validated_data):
        return MP4Updater(instance).update_size(**validated_data)
        
class MP4GetSerializer(_MP4Serializer): 
    class Meta(_MP4Serializer.Meta):
        fields = [
            'id',
            'filename',
            'processing',
            'processing_success',
        ]

class MP4DeleteSerializer(_MP4Serializer, toRepresentationMixin):
    class Meta(_MP4Serializer.Meta):
        fields = []