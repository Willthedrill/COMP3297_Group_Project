from rest_framework.decorators import api_view
from grpc import Status
from .models import VenueRecord
from .serializers import *
from django.http import HttpResponse
from rest_framework.response import Response
import pandas as pd
# Create your views here.

  
def create_venue_record(venue_code,location,type,capacity):
    #error mechanism
    '''
    venue record should be a dictionary containing code, location, type, capacity

    input constraints
    '''
    try:
        status=True
        error_message='error exist'
        success_message='successfully created item with the following record: '+venue_code+'//'+location+'//'+type+'//'+str(capacity)
        # try:
        if len(venue_code)>20:
            status=False
            error_message='length of venue code can not exceeed 20 characters'
        elif len(location)>150:
            status=False
            error_message='length of location can not exceeed 150 characters'
        elif type not in ['LT','CR','TR']:
            status=False
            error_message="type must be among ['LT','CR','TR'], standing for Lecture Theatre, Classroom and Tutor Room respectively"
        elif capacity<0:
            status=False
            error_message='capacity needs to be positive integer not exceeding 150'
        if status:
            p=VenueRecord(venue_code=venue_code,location=location,type=type,capacity=int(capacity))
            p.save()
            return status,success_message
        else:
            return status,error_message
    except Exception as e:
        return False,str(Exception)

def list_all_venue_record():
    try:
        status=True
        venue_record=VenueRecord.objects.all().order_by('venue_code')
        venue_record_serializer=VenueRecordSerializer(venue_record,many=True)
        message='success'
        return status,message,venue_record_serializer.data
    except Exception as e:
        return False,str(e),0

def view_venue_record(venue_code):
    try:
        venue_record=VenueRecord.objects.filter(venue_code=venue_code)
        venue_record_serialized=VenueRecordSerializer(venue_record,many=True)
        if len(venue_record)==0:
            message='No existing record for '+str(venue_code)
            return False,message,0
        return True,'success',venue_record_serialized.data
    except Exception as e:
        return False,str(e),0
    

def modify_venue_record(venue_code,location,type,capacity):
    try:
        p = VenueRecord.objects.get(venue_code=venue_code)
        p.location = location
        p.type = type
        p.capacity = capacity
        p.save()
        message='Successfully modified venue '+venue_code+'//'+location+'//'+type+'//'+str(capacity)
        return True,message
    except Exception as e:
        return False,str(e)

def delete_venue_record(venue_code):
    try:
        p = VenueRecord.objects.get(venue_code=venue_code)
        p.delete()
        message='Successfully Deleted venue '+str(venue_code)
        return True
    except Exception as e:
        return False,str(e)

