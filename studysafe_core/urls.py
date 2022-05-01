from . import views
from django.urls import path
from . import api_view
from . import records
from . import trace_api
urlpatterns = [
    path('api_device',api_view.index),
    path('api_trace',trace_api.get_close_contact),
    path('create_venue_record/<str:venue_code>/<str:location>/<str:type>/<int:capacity>',views.create_venue_record),
    path('list_all_venue_record',views.list_all_venue_record),
    path('modify_venue_record/<str:venue_code>/<str:location>/<str:type>/<int:capacity>',views.modify_venue_record),
    path('view_venue_record/<str:venue_code>',views.view_venue_record),
    path('delete_venue_record/<str:venue_code>',views.delete_venue_record),
    path('create_visit_record/<int:hkuid>/<str:venueid>/<str:datetime>/<str:type>',records.create_record),
    path('modify_visit_record/<int:hkuid>/<str:venueid>/<str:datetime>/<str:type>',records.modify_record),
    path('delete_visit_record/<str:recordid>',records.delete_record),
    path('view_all_visit_records',records.view_all_records),
]

