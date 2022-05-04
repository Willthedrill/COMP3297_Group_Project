from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import Record
from .serializers import *
from rest_framework.response import Response

def create_record(hkuid, venue_code, datetime, type):
    status=True
    try:
        p = Record(hkuid_id=hkuid, venue_code_id=venue_code, datetime=datetime, type=type)
        message='Successfully Created record'
        p.save()
        return status,message,p
    except Exception as e:
        status=False,
        message="Error in creating the record with error "+str(e)
        return status,message,p
    


def modify_record(recordid, hkuid, venue_code, datetime, type):
    status=True
    try:
        p = Record.objects.get(pk=recordid)
        message='Successful'
    except Exception as e:
        status=False
        message="Error: No such record ID! Exact Reasons: "+str(e)
    p.hkuid = hkuid
    p.venue_code = venue_code
    p.datetime = datetime
    p.type = type
    p.save()
    return status,message,p


def delete_record(recordid):
    status=True
    try:
        p = Record.objects.get(pk=int(recordid))
        p.delete()
        message='Successfully deleted'
        return status,message
    except Exception as e:
        status=False
        message="Error: No such record ID! Exact Error Message: "+str(e)
        return status,message

def view_all_records():
    status=True
    try:
        records = Record.objects.all().values()
        records_serialized=RecordSerializer(records,many=True)
        if len(records) == 0:
            message="Warning: no record available"
            return status,message,records_serialized.data
        else:
            return status,'success',records_serialized.data
    except Exception as e:
        return False,str(e),0