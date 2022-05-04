from django.urls import path
from . import views
urlpatterns = [
    path('trace_venue/<str:hkuid>/<str:infectious_time>',views.trace_venue.as_view()),    
]

