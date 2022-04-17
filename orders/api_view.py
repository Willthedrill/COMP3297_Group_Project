import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.records import *
from orders.members import *
@api_view(['POST',])
def index(request):
    str1 = request.data
    str1 = json.dumps(str1)
    query = json.loads(str1)
    if query['type']=='create':
        list=query['content']
        for i in list:
            #str=InsertMember(i['hkuid'],i['name']) llh
            #return Response({"state":"success"})
            recordid=create_record(i['hkuid'],i['venue'],i['datetime'],i['type'])
            return Response({"state":"success","cmd":"create","hkuid":i['hkuid'],"recordid":recordid,"venue":i['venue'],"datetime":i['datetime']})
    elif query['type']=='modify':
        list = query['content']
        for i in list:
            modify_record(i['recordid'],i['hkuid'], i['venue'], i['datetime'])
            return {"state": "success", "cmd": "modify", "hkuid": i['hkuid'], "recordid": i["recordid"], "venue": i['venue'],
                    "datetime": i['datetime']}
    elif query['type'] == 'delete':
        list = query['content']
        for i in list:
            DeleteMember(i['hkuid'])
            return Response({"i":i['hkuid']})
            #delete_record(i['recordid'])
            #return {"state": "success", "cmd": "delete","recordid": i["recordid"]}
    return {"state":"fail"}
