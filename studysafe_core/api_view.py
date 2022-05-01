from email import message
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from studysafe_core.records import *
from studysafe_core.members import *
@api_view(['POST',])
def index(request):
    str1 = request.data
    str1 = json.dumps(str1)
    query = json.loads(str1)
    if query['type']=='create':
        list_1=query['content']
        for i in list_1:
            #str=InsertMember(i['hkuid'],i['name']) llh
            #return Response({"state":"success"})
            status,message,p=create_record(i['hkuid'],i['venue'],i['datetime'],i['type'])
            if status:
                return Response({"state":"success","cmd":"create","hkuid":i['hkuid'],"recordid":p.pk,"venue":i['venue'],"datetime":i['datetime']})
            else:
                return Response(message)
    elif query['type']=='modify':
        list_1 = query['content']
        for i in list_1:
            status,message,p=modify_record(i['recordid'],i['hkuid'], i['venue'], i['datetime'],i['type'])
            if status:
                return Response({"state": "success", "cmd": "modify", "hkuid": i['hkuid'], "recordid": i["recordid"], "venue": i['venue'],"datetime": i['datetime'],"type":i['type']})
            else:
                return Response(message)
    elif query['type'] == 'delete':
        list_1 = query['content']
        for i in list_1:
            # DeleteMember(i['hkuid'])
            # return Response({"i":i['hkuid']})
            status,message=delete_record(i['recordid'])
            if status:
                return Response({"state": "success", "cmd": "delete","recordid": i["recordid"]})
            else:
                return HttpResponse(message)
    elif query['type']== 'list':
        '''
        to view the response value in pandas dataframe properly, use the following code: 
        import pandas as pd
        pd.DataFrame(response.json())
        '''
        all_record=view_all_records()
        return Response(all_record)


    return {"state":"fail"}
