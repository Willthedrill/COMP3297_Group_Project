
from django.http import HttpResponse
from .models import Record
from .serializers import *
from rest_framework.response import Response
import json
def create_record(request,hkuid, venue_code, datetime, type):
    status=True
    try:
        p = Record(hkuid_id=hkuid, venue_code_id=venue_code, datetime=datetime, type=type)
        message='Successfully Created record'+str(p.pk)
        p.save()
    except Exception as e:
        status=False,
        message="Error in creating the record with error "+str(e)
    return status,message,p


def modify_record(request,recordid, hkuid, venue_code, datetime, type):
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


def delete_record(request,recordid):
    status=True
    try:
        p = Record.objects.get(pk=recordid)
        p.delete()
        message='Successfully deleted'
    except Exception as e:
        status=False
        message="Error: No such record ID! Exact Error Message: "+str(e)
    return status,message


def view_all_records(request):
    records = Record.objects.all().values()
    records_serialized=RecordSerializer(records,manay=True)
    if len(records) == 0:
        records="Warning: no record available"
        return Response(records_serialized)
    else:
        return Response(records_serialized)
