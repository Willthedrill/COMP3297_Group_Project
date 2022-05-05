from matplotlib.style import context
from rest_framework.decorators import api_view
# import sys
# sys.append('../studysafe_core')
from studysafe_core.models import *
from studysafe_core.serializers import *
from rest_framework.response import Response
from django.views.generic import TemplateView

class trace_venue(TemplateView):
    template_name = "venues.html"
    def get_context_data(self, **kwargs):
        import pandas as pd
        import datetime
        hkuid,infectious_time_str=self.kwargs['hkuid'],self.kwargs['infectious_time']
        infectious_time=pd.to_datetime(infectious_time_str,format="%Y-%m-%d_%H:%M:%S")
        start_infectious_time=infectious_time+datetime.timedelta(days=-2)
        records = Record.objects.all().values()
        records=pd.DataFrame(records)
        records['datetime']=records['datetime'].apply(lambda x:pd.to_datetime(x,format="%Y-%m-%d %H:%M:%S"))
        temp_records=records.loc[records['hkuid_id']==hkuid]
        venue_record=temp_records.loc[temp_records['datetime'].apply(lambda x:True if ((x<infectious_time)and (x>start_infectious_time)) else False)].sort_values('venue_code_id')
        context={}
        context['subject']=hkuid
        context['date']=infectious_time_str
        context['venues']=list(venue_record['venue_code_id'].drop_duplicates().sort_values())
        return context


