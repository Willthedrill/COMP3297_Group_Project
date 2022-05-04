from datetime import datetime
from rest_framework import serializers




class MemberRecordSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    hkuid=serializers.CharField(max_length=10)
    name=serializers.CharField(max_length=150)

class VenueRecordSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    venue_code=serializers.CharField(max_length=20)
    location=serializers.CharField(max_length=150)
    type=serializers.CharField(max_length=2)
    capacity=serializers.IntegerField()

class RecordSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    hkuid_id=serializers.CharField()    
    venue_code_id=serializers.CharField(max_length=20)
    datetime=serializers.CharField(max_length=30)
    type=serializers.CharField(max_length=2)