from models import venue
from datetime import datetime

from orders.models import Record


def create_record(hkuid, venueid, datetime):

    try:
        p = Record(hkuid=hkuid, venueid=venueid, datetime=datetime)
    except:
        return "Error in creating the record"
    p.save()
    return "Record created successfully!"


def modify_record(recordid, hkuid, venue, datetime):
    try:
        p = Record.objects.get(pk=recordid)
    except:
        return "Error: No such record ID!"
    p.hkuid = hkuid
    p.venue = venue
    p.datetime = datetime
    p.save()
    return "Record updated successfully!"


def delete_record(recordid):
    try:
        p = Record.objects.get(pk=recordid)
    except:
        return "Error: No such record ID!"
    p.delete()
    return "Record deleted successfully!"


def get_records():
    records = Record.object.all()
    if len(records) == 0:
        return "Warning: no record available"
    else:
        return records
