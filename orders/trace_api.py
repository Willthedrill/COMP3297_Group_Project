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
#    list=query['content']
    uid= query.hkuid
    d= query.datetime
    date= datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
    beforeone= datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')- timedelta(days=1)
    beforetwo= datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')- timedelta(days=2)
    result=[]
    result_venue=[]
    message=[]
    subject={"hkuid":uid,"datetime":date}
    history=Record.objects.filter(hkuid=uid, type='en')
    for list in history:
        date1= list.datetime
        t=datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
        if (t.date== date.date or t.date()== beforeone.date() or t.date()== beforetwo.date()):
            result_venue.append(list.venue)
        #result_venue= venues the infected person went to in the last two days
        for venue in result_venue:
            close_contact=Record.objects.filter(type='en', venue=venue)
            for individual in close_contact:
                datetime2= individual.datetime
                t2=datetime.datetime.strptime(datetime2, '%Y-%m-%d %H:%M:%S')
                if (t2.date()== date.date() or t2.date()== beforeone.date() or t2.date()== beforetwo.date()):
                    message.append({"hkuid":individual.hkuid, "venue":individual.venue, "subject":subject})
                   
                    
    if len(result)==0:
        return "No close contacts available"
    else:    
        return Response(message)
        
    
    
    
