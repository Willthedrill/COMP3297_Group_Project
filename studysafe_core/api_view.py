from email import message
import json
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from studysafe_core.records import *
from studysafe_core.members import *
from studysafe_core.views import *

def check(status,message):
    if status:
        return str(message)
    else:
        return 'failed with error: '+str(message)

@api_view(['POST',])
def index(request):
    str1 = request.data
    str1 = json.dumps(str1)
    query = json.loads(str1)
    response_list=[]
    #modifications on records
    if query['type']=='create':
        list_1=query['content']
        for i in list_1:
            status,message,p=create_record(**i)
            response_list.append({"state":check(status,message),"cmd":"create","hkuid":i['hkuid'],"recordid":p.pk,"venue":i['venue_code'],"datetime":i['datetime']})
        return Response(response_list)
    elif query['type']=='modify':
        list_1 = query['content']
        for i in list_1:
            status,message,p=modify_record(i['recordid'],i['hkuid'], i['venue_code'], i['datetime'],i['type'])
            response_list.append({"state": check(status,message), "cmd": "modify", "hkuid": i['hkuid'], "recordid": i["recordid"], "venue": i['venue_code'],"datetime": i['datetime'],"type":i['type'],"message":message})
        return Response(response_list)
    elif query['type'] == 'delete':
        list_1 = query['content']
        for i in list_1:
            status,message=delete_record(**i)
            response_list.append({"state": check(status,message), "cmd": "delete","recordid": i["recordid"]})
        return Response(response_list)
            
    elif query['type']== 'list':
        '''
        to view the response value in pandas dataframe properly, use the following code: 
        import pandas as pd
        pd.DataFrame(response.json())
        '''
        status,message,all_record=view_all_records()
        response_list.append({'state':check(status,message),'cmd':'list_all','data':all_record})
        return Response(response_list)

    #manipulating venue record
    elif query['type']=='create_venue':
        list_1 = query['content']
        for i in list_1:
            status,message=create_venue_record(**i)
            response_list.append({'state':check(status,message)})
        return Response(response_list)
    elif query['type']=='list_all_venue':
        status,message,all_record=list_all_venue_record()
        response_list.append({'state':check(status,message),'cmd':'list_all','data':all_record})
        return Response(response_list)
    elif query['type']=='view_venue':
        list_1 = query['content']
        for i in list_1:
            print(type(i))
            status,message=view_venue_record(**i)
            response_list.append({'state':check(status,message)})
        return Response(response_list)
    elif query['type']=='modify_venue':
        list_1 = query['content']
        for i in list_1:
            status,message=view_venue_record(**i)
            response_list.append({'state':check(status,message)})
        return Response(response_list)
    elif query['type']=='delete_venue':
        list_1 = query['content']
        for i in list_1:
            status,message=delete_venue_record(**i)
            response_list.append({'state':check(status,message)})
        return Response(response_list) 

    #manipulating student records
    elif query['type']=='create_student':
        list_1 = query['content']
        for i in list_1:
            status,message=InsertMember(**i)
            response_list.append({'state':check(status,message)})
        return Response(response_list) 
    
    elif query['type']=='delete_student':
        list_1 = query['content']
        for i in list_1:
            status,message=DeleteMember(**i)
            response_list.append({'state':check(status,message)})
        return Response(response_list) 

    elif query['type']=='list_all_students':
        status,message,all_record=ListAllMember()
        response_list.append({'state':check(status,message),'cmd':'list_all','data':all_record})
        return Response(response_list)

    elif query['type']=='search_student':
        #fields required: hkuid, name
        list_1 = query['content']
        for i in list_1:
            status,message,all_record=SearchMember(**i)
            response_list.append({'state':check(status,message),'cmd':'search_student','data':all_record})
        return Response(response_list)
    elif query['type']=='update_student':
        list_1 = query['content']
        for i in list_1:
            status,message=UpdateMember(**i)
            response_list.append({'state':check(status,message)})
        return Response(response_list) 


    
    return Response({"state":"failed, please recheck whether your commmand is correct or not"})
