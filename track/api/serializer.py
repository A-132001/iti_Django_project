from rest_framework import serializers
from ..models import Track
class Track_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    department = serializers.CharField(max_length=50)
    location =  serializers.CharField(max_length=50)
    createdate=serializers.DateTimeField()
    updatedate=serializers.DateTimeField()
    isactive=serializers.BooleanField()
    
    @classmethod
    def get_and_turn_all_to_json(cls):
        all_tracks = Track.objects.all()
        turned_tracks = cls(all_tracks, many=True)
        return turned_tracks.data
    
    @classmethod
    def get_track_by_id(cls,id):
        return Track_Serializer(Track.objects.get(id=id)).data
    
    def update(self, instance, validated_data):
        instance.name=validated_data['name']
        instance.location=validated_data['location']
        instance.department=validated_data['department']
        instance.save()
        return instance
