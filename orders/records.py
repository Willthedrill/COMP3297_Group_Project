from models import venue
from datetime import datetime

from orders.models import Record


def create_record(hkuid, venueid, datetime, type):
    try:
        p = Record(hkuid=hkuid, venueid=venueid, datetime=datetime, type=type)
    except:
        return "Error in creating the record"
    p.save()
    return p.pk


def modify_record(recordid, hkuid, venue, datetime, type):
    try:
        p = Record.objects.get(pk=recordid)
    except:
        return "Error: No such record ID!"
    p.hkuid = hkuid
    p.venue = venue
    p.datetime = datetime
    p.type = type
    p.save()
    return p.pk


def delete_record(recordid):
    try:
        p = Record.objects.get(pk=recordid)
    except:
        return "Error: No such record ID!"
    p.delete()
    return "Record deleted successfully"


def get_records():
    records = Record.object.all()
    if len(records) == 0:
        return "Warning: no record available"
    else:
        return records
