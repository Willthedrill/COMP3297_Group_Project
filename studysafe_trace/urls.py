from django.urls import path
from . import views
urlpatterns = [
    path('trace_venue/<str:hkuid>/<str:infectious_time>',views.trace_venue.as_view()),
    path('trace_contacts/<str:hkuid>/<str:datetime>', views.contacts),
]

