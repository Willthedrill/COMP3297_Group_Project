from orders import views
from django.urls import path
from orders import api_view
urlpatterns = [
    path('apitest',api_view.index),
]
