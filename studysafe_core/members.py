from .models import MemberRecord
import json
from .serializers import *
def InsertMember(hkuid, name):
    try:
        uid=hkuid
        NewMember = MemberRecord.objects.get(hkuid = uid)
    except:
        uid=hkuid
        if (len(uid) != 10 and len(uid) != 5) or not uid.isnumeric():
            message = json.dumps({"hkuid":uid, "message":"Error: invalid HKU ID format, should be 10 numbers."})
            return message
        if len(name) == 0 or len(name) > 150:
            message = json.dumps({"hkuid":uid, "message":"Error: invalid name length, should be 1 - 150."})
            return True,message
        NewMember = MemberRecord(hkuid = uid, name = name)
        NewMember.save()
        message = json.dumps({"hkuid":uid, "message":"HKU member record created successfully."})
        return True,message
    message = json.dumps({"hkuid":uid, "message":"Error: record with such HKU ID already exists."})
    return False,message

def UpdateMember(hkuid, name):
    try:
        uid=hkuid
        member = MemberRecord.objects.get(hkuid = uid)
    except Exception as e:
        uid=hkuid
        message = json.dumps({"hkuid":uid, "message":"Error: given HKU ID does not match any records.","keyerror":str(e)})
        return False,message
    if len(name) == 0 or len(name) > 150:
        message = json.dumps({"hkuid":uid, "message":"Error: invalid name length, should be 1 - 150."})
        return False,message
    member.name = name
    member.save()
    message = json.dumps({"hkuid":uid, "message":"HKU member record updated successfully."})
    return True,message

def SearchMember(hkuid):
    key=hkuid
    try:
        member = MemberRecord.objects.get(hkuid = key)
        members_serializer=MemberRecordSerializer(member)
    except:
        try:
            member = MemberRecord.objects.get(name = key)
            members_serializer=MemberRecordSerializer(member,many=True)
        except Exception as e:
            message = json.dumps({"key_error":str(e), "message":"Error: given HKU ID or name does not match any records."})
            return False,message,0
        message = json.dumps({"hkuid":member.hkuid,"name":member.name})
        return False,message,0
    message = json.dumps({"hkuid":member.hkuid,"name":member.name})
    return True,message,members_serializer.data

def DeleteMember(hkuid):
    uid=hkuid
    try:
        member = MemberRecord.objects.get(hkuid = uid)
    except:
        message = json.dumps({"hkuid":uid, "message":"Error: given HKU ID does not match any records."})
        return False,message
    member.delete()
    message = json.dumps({"hkuid":uid, "message":"HKU member record deleted successfully."})
    return True,message

def ListAllMember():
    members = MemberRecord.objects.all().order_by('hkuid')
    members_serializer=MemberRecordSerializer(members,many=True)
    if len(members) == 0:
        message = json.dumps({"message":"Warning: no record available."})
        return False,message,0
    else:
        message = []
        for member in members:
            message.append({"hkuid":member.hkuid, "name":member.name})
        message = sorted(message, key=lambda d: d['hkuid'])
        message = json.dumps(message)
        return True,message,members_serializer.data
