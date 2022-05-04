
from django.http import HttpResponse
from .models import Record


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
    if len(records) == 0:
        records="Warning: no record available"
        return HttpResponse(content=records)
    else:
        return HttpResponse(records)
