from .models import MemberRecord

def InsertMember(uid, name):
    try:
        NewMember = MemberRecord.get(uid = uid)
    except:
        if len(uid) != 10 or not uid.isnumeric():
            return "Error: invalid HKU ID format, should be 10 numbers."
        if len(name) == 0 or len(name) > 150:
            return "Error: invalid name length, should be 1 - 150."
        NewMember = MemberRecord(uid = uid, name = name)
        NewMember.save()
        return "HKU member record created successfully."
    return "Error: record with such HKU ID already exists"

def UpdateMember(uid, name):
    try:
        member = MemberRecord.get(uid = uid)
    except:
        return "Error: given HKU ID does not match any records"
    if len(name) == 0 or len(name) > 150:
        return "Error: invalid name length, should be 1 - 150."
    member.name = name
    member.save()
    return "HKU member record updated successfully."

def SearchMember(key):
    try:
        member = MemberRecord.get(uid = key)
    except:
        try:
            member = MemberRecord.get(name = key)
        except:
            return "Error: given HKU ID or name does not match any records"
    return member

def DeleteMember(uid):
    try:
        member = MemberRecord.get(uid = uid)
    except:
        return "Error: given HKU ID does not match any records"
    member.delete()
    return "HKU member record deleted successfully."

def ListAllMember():
    members = MemberRecord.objects.all()
    if len(members) == 0:
        return "Warning: no record available"
    else:
        return members