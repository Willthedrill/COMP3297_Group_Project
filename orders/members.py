from .models import MemberRecord
import json
def InsertMember(uid, name):
    try:
        NewMember = MemberRecord.get(uid = uid)
    except:
        if len(uid) != 10 or not uid.isnumeric():
            message = json.dump({"hkuid":uid, "message":"Error: invalid HKU ID format, should be 10 numbers."})
            return message
        if len(name) == 0 or len(name) > 150:
            message = json.dump({"hkuid":uid, "message":"Error: invalid name length, should be 1 - 150."})
            return message
        NewMember = MemberRecord(uid = uid, name = name)
        NewMember.save()
        message = json.dump({"hkuid":uid, "message":"HKU member record created successfully."})
        return message
    message = json.dump({"hkuid":uid, "message":"Error: record with such HKU ID already exists."})
    return message

def UpdateMember(uid, name):
    try:
        member = MemberRecord.get(uid = uid)
    except:
        message = json.dump({"hkuid":uid, "message":"Error: given HKU ID does not match any records."})
        return message
    if len(name) == 0 or len(name) > 150:
        message = json.dump({"hkuid":uid, "message":"Error: invalid name length, should be 1 - 150."})
        return message
    member.name = name
    member.save()
    message = json.dump({"hkuid":uid, "message":"HKU member record updated successfully."})
    return message

def SearchMember(key):
    try:
        member = MemberRecord.get(uid = key)
    except:
        try:
            member = MemberRecord.get(name = key)
        except:
            message = json.dump({"hkuid":uid, "message":"Error: given HKU ID or name does not match any records."})
            return message
        message = json.dump(member)
        return message
    message = json.dump(member)
    return message

def DeleteMember(uid):
    try:
        member = MemberRecord.get(uid = uid)
    except:
        message = json.dump({"hkuid":uid, "message":"Error: given HKU ID does not match any records."})
        return message
    member.delete()
    message = json.dump({"hkuid":uid, "message":"HKU member record deleted successfully."})
    return message

def ListAllMember():
    members = MemberRecord.objects.all()
    if len(members) == 0:
        message = json.dump({"hkuid":uid, "Warning: no record available."})
        return message
    else:
        message = json.dump(members)
        return message
