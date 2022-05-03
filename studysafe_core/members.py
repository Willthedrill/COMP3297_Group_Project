from .models import MemberRecord
import json
def InsertMember(uid, name):
    try:
        NewMember = MemberRecord.objects.get(hkuid = uid)
    except:
        iif (len(uid) != 10 and len(uid) != 5) or not uid.isnumeric():
            message = json.dumps({"hkuid":uid, "message":"Error: invalid HKU ID format, should be 10 numbers."})
            return message
        if len(name) == 0 or len(name) > 150:
            message = json.dumps({"hkuid":uid, "message":"Error: invalid name length, should be 1 - 150."})
            return message
        NewMember = MemberRecord(hkuid = uid, name = name)
        NewMember.save()
        message = json.dumps({"hkuid":uid, "message":"HKU member record created successfully."})
        return message
    message = json.dumps({"hkuid":uid, "message":"Error: record with such HKU ID already exists."})
    return message

def UpdateMember(uid, name):
    try:
        member = MemberRecord.objects.get(hkuid = uid)
    except:
        message = json.dumps({"hkuid":uid, "message":"Error: given HKU ID does not match any records."})
        return message
    if len(name) == 0 or len(name) > 150:
        message = json.dumps({"hkuid":uid, "message":"Error: invalid name length, should be 1 - 150."})
        return message
    member.name = name
    member.save()
    message = json.dumps({"hkuid":uid, "message":"HKU member record updated successfully."})
    return message

def SearchMember(key):
    try:
        member = MemberRecord.objects.get(hkuid = key)
    except:
        try:
            member = MemberRecord.objects.get(name = key)
        except:
            message = json.dumps({"key":key, "message":"Error: given HKU ID or name does not match any records."})
            return message
        message = json.dumps({"hkuid":member.hkuid,"name":member.name})
        return message
    message = json.dumps({"hkuid":member.hkuid,"name":member.name})
    return message

def DeleteMember(uid):
    try:
        member = MemberRecord.objects.get(hkuid = uid)
    except:
        message = json.dumps({"hkuid":uid, "message":"Error: given HKU ID does not match any records."})
        return message
    member.delete()
    message = json.dumps({"hkuid":uid, "message":"HKU member record deleted successfully."})
    return message

def ListAllMember():
    members = MemberRecord.objects.all()
    if len(members) == 0:
        message = json.dumps({"message":"Warning: no record available."})
        return message
    else:
        message = []
        for member in members:
            message.append({"hkuid":member.hkuid, "name":member.name})
        message = sorted(message, key=lambda d: d['hkuid'])
        message = json.dumps(message)
        return message
