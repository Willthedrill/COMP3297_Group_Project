from .models import MemberRecord
import json
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
    except:
        uid=hkuid
        message = json.dumps({"hkuid":uid, "message":"Error: given HKU ID does not match any records."})
        return False,message
    if len(name) == 0 or len(name) > 150:
        message = json.dumps({"hkuid":uid, "message":"Error: invalid name length, should be 1 - 150."})
        return False,message
    member.name = name
    member.save()
    message = json.dumps({"hkuid":uid, "message":"HKU member record updated successfully."})
    return True,message

def SearchMember(key):
    try:
        member = MemberRecord.objects.get(hkuid = key)
    except:
        try:
            member = MemberRecord.objects.get(name = key)
        except:
            message = json.dumps({"key":key, "message":"Error: given HKU ID or name does not match any records."})
            return False,message
        message = json.dumps({"hkuid":member.hkuid,"name":member.name})
        return True,message
    message = json.dumps({"hkuid":member.hkuid,"name":member.name})
    return True,message

def DeleteMember(uid):
    try:
        member = MemberRecord.objects.get(hkuid = uid)
    except:
        message = json.dumps({"hkuid":uid, "message":"Error: given HKU ID does not match any records."})
        return False,message
    member.delete()
    message = json.dumps({"hkuid":uid, "message":"HKU member record deleted successfully."})
    return True,message

def ListAllMember():
    members = MemberRecord.objects.all()
    if len(members) == 0:
        message = json.dumps({"message":"Warning: no record available."})
        return False,message
    else:
        message = []
        for member in members:
            message.append({"hkuid":member.hkuid, "name":member.name})
        message = sorted(message, key=lambda d: d['hkuid'])
        message = json.dumps(message)
        return True,message
