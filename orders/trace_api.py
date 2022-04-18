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
    uid= query['hkuid']
    d= query['datetime']
    date= datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
    beforeone= datetime.strptime(d, '%Y-%m-%d %H:%M:%S')- timedelta(days=1)
    beforetwo= datetime.strptime(d, '%Y-%m-%d %H:%M:%S')- timedelta(days=2)
    result_venue=[]
    result=[]
    subject=[]
    history=Record.objects.filter(hkuid=uid, type='en')
   # history=json.loads(filter)
    print(history)
    for list in history:
        print(list)
        datetime1= list.datetime
        t=datetime.strptime(datetime1, '%Y-%m-%d %H:%M:%S')
        if (t.getDate()== date.getDate() or t.getDate()== beforeone.getDate() or t.getDate()== beforetwo.getDate()):
            result_venue.append(list['venue'])
        #result_venue= venues the infected person went to in the last two days
        for venue in result_venue:
            close_contact=Record.objects.filter(type='en', venue=venue)
            for individual in close_contact:
                datetime2= individual['datetime']
                t2=datetime.strptime(datetime2, '%Y-%m-%d %H:%M:%S')
                if (t2.getDate()== date.getDate() or t2.getDate()== beforeone.getDate() or t2.getDate()== beforetwo.getDate()):
                    result.append(individual["hkuid"]) #,individual['name'])
                    subject.append(individual)
    if len(result)==0:
        return "No close contacts available"
    else:    
        for i in len(result):
           return {"close contact":result[i],"venue":result_venue[i],"subject":subject[i]}
        
    
    
    
    
    
    
  
