from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from datetime import timedelta, datetime
from .models import *
def handle_date(datetime1):
    result=datetime1.strftime("%Y-%m-%d")
    result=datetime.strptime(result,'%Y-%m-%d')
    return result

@api_view(['POST',])
def get_close_contact(request):
    str1=request.data
    str1=json.dumps(str1)
    query=json.loads(str1)
    uid=query['hkuid']
    date=query['datetime']
    history = Record.objects.filter(hkuid=uid, type='EN')
    print(history)
    d = handle_date(datetime.strptime(date, '%Y-%m-%d %H:%M:%S'))
    beforeone = handle_date(datetime.strptime(date, '%Y-%m-%d %H:%M:%S') - timedelta(days=1))
    beforetwo = handle_date(datetime.strptime(date, '%Y-%m-%d %H:%M:%S') - timedelta(days=2))
    dic={}
    for i in history:
        temp = handle_date(datetime.strptime(i.datetime, '%Y-%m-%d %H:%M:%S'))
        if (temp == d or temp==beforeone or temp==beforetwo):
            dic[i.venue_code]=i.venue_code
    dic2={}
    for k in dic:
        rec=Record.objects.filter(venue_code=k, type='EN')
        for m in rec:
            temp=handle_date(datetime.strptime(m.datetime, '%Y-%m-%d %H:%M:%S'))
            if (temp == d or temp == beforeone or temp == beforetwo) and m.hkuid!=query['hkuid']:
                dic2[m.hkuid] = m.hkuid
    result={"venue_code":[],"contacts":[],"subject":"none"}
    for i in dic:
        temp={'name':i.venue_code}
        result['venue_code'].append(temp)
    for f in dic2:
        temp={'hkuid':f.hkuid}
        result['contacts'].append(temp)
    temp2={"hkuid":query['hkuid'],"datetime":query['datetime']}
    result["subject"]=temp2
    p=0
    for m in result['contacts']:
        if m['hkuid']==query['hkuid']:
            del result['contacts'][0]
        p=p+1
    return Response(result)


