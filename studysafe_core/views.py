from rest_framework.decorators import api_view
from grpc import Status
from .models import VenueRecord
from .serializers import *
from django.http import HttpResponse
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])       
def create_venue_record(request,venue_code,location,type,capacity):
    #error mechanism
    '''
    venue record should be a dictionary containing code, location, type, capacity
    '''
    error_exist=False
    error_message='error exist'
    success_message='successfully created item with the following record: '+venue_code+'//'+location+'//'+type+'//'+str(capacity)
    # try:
    if len(venue_code)>20:
        error_exist=True
        error_message='length of venue code can not exceeed 20 characters'
    elif len(location)>150:
        error_exist=True
        error_message='length of location can not exceeed 150 characters'
    elif type not in ['LT','CR','TR']:
        error_exist=True
        error_message="type must be among ['LT','CR','TR'], standing for Lecture Theatre, Classroom and Tutor Room respectively"
    elif capacity<0:
        error_exist=True
        error_message='capacity needs to be positive integer not exceeding 150'
    if not error_exist:
        print(type(capacity))
        p=VenueRecord(venue_code=venue_code,location=location,type=type,capacity=capacity)
        p.save()
        return Response(success_message)
    else:
        return Response(error_message)
    # except:
    #     return HttpResponse(error_message)
@api_view(['GET'])
def list_all_venue_record(request):
    venue_record=VenueRecord.objects.all()
    venue_record_serializer=VenueRecordSerializer(venue_record,many=True)
    return Response(venue_record_serializer.data)
@api_view(['GET'])
def view_venue_record(request,venue_code):
    venue_record=VenueRecord.objects.filter(venue_code=venue_code)
    venue_record_serialized=VenueRecordSerializer(venue_record,many=True)
    if len(venue_record)==0:
        p='No existing record for '+str(venue_code)
        return Response(p)
    return Response(venue_record_serialized.data)
    
@api_view(['GET','POST'])
def modify_venue_record(request,venue_code,location,type,capacity):
    p = VenueRecord.objects.get(venue_code=venue_code)
    p.location = location
    p.type = type
    p.capacity = capacity
    p.save()
    return Response(Status=200)

@api_view(['GET','POST'])
def delete_venue_record(request,venue_code):
    p = VenueRecord.objects.get(venue_code=venue_code)

    p.delete()
    return Response(Status=200)
