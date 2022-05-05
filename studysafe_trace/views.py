from matplotlib.style import context
from rest_framework.decorators import api_view
# import sys
# sys.append('../studysafe_core')
from studysafe_core.models import *
from studysafe_core.serializers import *
from rest_framework.response import Response
from django.views.generic import TemplateView
import json
import requests
class trace_venue(TemplateView):
    
    template_name = "venues.html"
    def get_context_data(self, **kwargs):
        def display_detail(response,return_df=False):
            raw=json.loads(response.content.decode('utf-8'))
            for i in range(len(raw)):
                try:
                    if not return_df:
                        display(pd.DataFrame(raw[i]['data']))
                except:
                    display(raw[i])
            if return_df:
                try:
                    return pd.DataFrame(raw[0]['data'])
                except:
                    pass
        import pandas as pd
        import datetime
        hkuid,infectious_time_str=self.kwargs['hkuid'],self.kwargs['infectious_time']
        infectious_time=pd.to_datetime(infectious_time_str,format="%Y-%m-%d_%H:%M:%S")
        start_infectious_time=infectious_time+datetime.timedelta(days=-2)
        local=True
        params={"type":"list"}
        remote_core_path="https://shielded-tor-28383.herokuapp.com/studysafe_core/api_device"
        local_core_path='http://localhost:8000/studysafe_core'
        if local:
            response=requests.post(local_core_path+'/api_device',data=json.dumps(params),headers = {'content-type':'application/json'})
        else:
            response=requests.post(remote_core_path+'/api_device',data=json.dumps(params),headers = {'content-type':'application/json'})
        records=display_detail(response,return_df=True)
        records['datetime']=records['datetime'].apply(lambda x:pd.to_datetime(x,format="%Y-%m-%d %H:%M:%S"))
        temp_records=records.loc[records['hkuid_id']==hkuid]
        venue_record=temp_records.loc[temp_records['datetime'].apply(lambda x:True if ((x<infectious_time)and (x>start_infectious_time)) else False)].sort_values('venue_code_id')
        context={}
        context['subject']=hkuid
        context['date']=infectious_time_str
        context['venues']=list(venue_record['venue_code_id'].drop_duplicates().sort_values())
        return context

from django.shortcuts import render
from functions import api
from functions import handle
def contacts(request,hkuid,datetime):
    #return HttpResponse("hello world")
    context=api.getdata(hkuid=hkuid,datetime=datetime)
    context2=handle.handledata(context)
    return render(request, 'contacts.html', context=context2)
