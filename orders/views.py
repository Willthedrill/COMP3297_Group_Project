from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from models import VenueRecord
# Create your views here.


def create_venue_record(request,venue_record):
    #error mechanism
    '''
    venue record should be a dictionary containing code, location, type, capacity
    '''
    error_exist=False
    error_message='error exist'
    success_message='successfully created item'
    for i in ['code','location','type','capacity']:
        if i not in venue_record.keys():
            error_exist=True
        if not error_exist:
            venue_code=venue_record['code']
            location=venue_record['location']
            type=venue_record['type']
            capacity=venue_record['capacity']
            p=VenueRecord(venue_code=venue_code,location=location,type=type,capacity=capacity)
            p.save()
            return success_message
        else:
            return error_message
    

        
def list_all_venue_record(request):
    venue_record=pd.DataFrame(VenueRecord.object.all())
    return venue_record

def view_venue_record(request,venue_code):
    #p=VenueRecord.objects.getall(pk=venue_code)
    sub=pd.DataFrame(p)
    sub=sub.loc[sub['venue_code']==venue_code]
    return 
    

def modify_venue_record():
    p = VenueRecord.objects.get(pk=venue_code)
    p.location = location
    p.type = type
    p.capacity = capacity
    p.save()
    return
def delete_venue_record():
    p = VenueRecord.objects.get(pk=venue_code)
    p.delete()
    return


