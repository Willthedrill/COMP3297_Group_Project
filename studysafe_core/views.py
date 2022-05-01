
from .models import VenueRecord

from django.http import HttpResponse

# Create your views here.


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
        return HttpResponse(success_message)
    else:
        return HttpResponse(error_message)
    # except:
    #     return HttpResponse(error_message)
        
def list_all_venue_record(request):
    venue_record=VenueRecord.objects.all()
    return HttpResponse(venue_record)

def view_venue_record(request,venue_code):
    p=VenueRecord.objects.filter(venue_code=venue_code)
    if len(p)==0:
        p='No existing record for '+str(venue_code)
    return HttpResponse(p)
    

def modify_venue_record(request,venue_code,location,type,capacity):
    p = VenueRecord.objects.get(venue_code=venue_code)
    p.location = location
    p.type = type
    p.capacity = capacity
    p.save()
    return
def delete_venue_record(request,venue_code):
    p = VenueRecord.objects.get(venue_code=venue_code)
    p.delete()
    return
