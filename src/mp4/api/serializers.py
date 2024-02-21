

from mp4.models import MP4
from rest_framework import serializers
from mp4.utils.makers import MP4Maker, MP4Updater


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
        return MP4Maker(**validated_data).create()

class MP4PartialUpdateSerializer(toRepresentationMixin, _MP4Serializer):
    
    width = serializers.IntegerField(write_only=True)
    height = serializers.IntegerField(write_only=True)
    
    class Meta(_MP4Serializer.Meta):
        fields = [
            'width',
            'height', 
        ]
    
    def update(self, instance, validated_data):
        return MP4Updater(instance).update_size(**validated_data)
    
    def validate_width(self, attr):
        return self._validate_hw(attr)
    
    def validate_height(self, attr):
        return self._validate_hw(attr)
    
    def _validate_hw(self, attr, high_limit=20):
        if attr > high_limit:
            raise serializers.ValidationError(
                {"end_date": "End date must be after start date."}
            )
        return attr
        
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