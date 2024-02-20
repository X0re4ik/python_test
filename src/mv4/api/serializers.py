

from mv4.models import MV4
from rest_framework import serializers
from mv4.utils.makers import MV4Maker, MV4Updater


class toRepresentationMixin:
    def to_representation(self, instance):
        return {
            "success": True
        }

class _MV4Serializer(serializers.ModelSerializer):
    class Meta:
        model = MV4
        
    

class MV4CreateSerializer(_MV4Serializer):
    file = serializers.FileField(write_only=True) 
    class Meta(_MV4Serializer.Meta):
        fields = [
            'id',
            'file',    
        ]
    
    def create(self, validated_data):
        return MV4Maker(**validated_data).create()

class MV4PartialUpdateSerializer(toRepresentationMixin, _MV4Serializer):
    
    width = serializers.IntegerField(write_only=True)
    height = serializers.IntegerField(write_only=True)
    
    class Meta(_MV4Serializer.Meta):
        fields = [
            'width',
            'height', 
        ]
    
    def update(self, instance, validated_data):
        return MV4Updater(instance).update_size(**validated_data)
    
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
        
class MV4GetSerializer(_MV4Serializer): 
    class Meta(_MV4Serializer.Meta):
        fields = [
            'id',
            'filename',
            'processing',
            'processing_success',
        ]

class MV4DeleteSerializer(_MV4Serializer, toRepresentationMixin):
    class Meta(_MV4Serializer.Meta):
        fields = []