from models import venue
from datetime import datetime

def create_record(hkuid, venueid, datetime):
    p = Record(hkuid=hkuid, venueid=venueid, datetime=datetime.now())
    p.save()
    return


def modify_record(recordid, hkuid, venue, datetime):
    p = Record.objects.get(pk=recordid)
    p.hkuid = hkuid
    p.venue = venue
    p.datetime = datetime
    p.save()
    return


def delete_record(recordid):
    p = Record.objects.get(pk=recordid)
    p.delete()
    return


def get_records():
    return Record.object.all()
