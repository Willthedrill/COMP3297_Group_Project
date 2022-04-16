from models import venue
from datetime import datetime


def create_record(hkuid, venueid, datetime):
    p = Record(hkuid=hkuid, venueid=venueid, datetime=datetime.strptime(
        datetime, '%Y-%m-%d %H:%M:%S'))
    p.save()
    return "Record created successfully!"


def modify_record(recordid, hkuid, venue, datetime):
    try:
        p = Record.objects.get(pk=recordid)
    except:
        return "We don't have this kind of record!"
    p.hkuid = hkuid
    p.venue = venue
    p.datetime = datetime.strptime(
        datetime, '%Y-%m-%d %H:%M:%S')
    p.save()
    return "Record updated successfully!"


def delete_record(recordid):
    try:
        p = Record.objects.get(pk=recordid)
    except:
        return "We don't have this kind of record!"
    p.delete()
    return "Record deleted successfully!"


def get_records():
    return Record.object.all()
