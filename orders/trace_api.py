from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from datetime import timedelta, datetime
from orders.models import *


@api_view(['POST',])

def get_close_contact(request):
    str1=request.data
    str1=json.dumps(str1)
    query=json.loads(str1)
    uid= query['hkuid']
    d= query['datetime']
    date= datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
    date_day= date.strftime("%Y-%m-%d")
    beforeone= datetime.strptime(d, '%Y-%m-%d %H:%M:%S')- timedelta(days=1)
    beforeone_day= beforeone.strftime("%Y-%m-%d")
    beforetwo= datetime.strptime(d, '%Y-%m-%d %H:%M:%S')- timedelta(days=2)
    beforetwo_day= beforetwo.strftime("%Y-%m-%d")
    result_venue=[]
    message={}
    subject={"hkuid":uid,"datetime":date}
    history=Record.objects.filter(hkuid=uid, type='en')
    for list in history:
        date1= list.datetime
        date1_day= date1.strftime("%Y-%m-%d")
        if (date1_day== date_day or date1_day== beforeone_day or date1_day== beforetwo_day):
            result_venue.append(list.venue)
    
        #result_venue= venues the infected person went to in the last two days (mb12/mb14
        i=0
        for venue in result_venue:
            close_contact=Record.objects.filter(type='en', venue=venue) #91/93\
            for individual in close_contact:
                datetime2= individual.datetime
                datetime2_day=datetime2.strftime("%Y-%m-%d")
                #t2=datetime.strptime(datetime2, '%Y-%m-%d %H:%M:%S')
                if (datetime2_day== date_day or datetime2_day== beforeone_day or datetime2_day== beforetwo_day) and (individual.hkuid != uid):
                    message[i]={}
                    message[i]['hkuid']= individual.hkuid
                    message[i]['venue']= individual.venue
                    message[i]['subject']= subject
                    i+=1
                
                     
    if len(message)==0:
        return Response({"No close contacts available"})
    else:    
        return Response(message)
      
