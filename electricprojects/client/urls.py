from django.urls import path

from . import views


app_name = "client"

urlpatterns = [
    path('add-client/', views.add_client, name='add_client'),
    path('ajax/possible-clients/', views.initial, name='initial')
]