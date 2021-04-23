from django.urls import path

from . import views


app_name = "client"

urlpatterns = [
    path('<int:id_client>/', views.edit_client_information, name='edit_client_information'),
    path('add-client/', views.add_client, name='add_client'),
    path('select-client/', views.select_client, name='select_client'),
    path('ajax/possible-clients/', views.initial, name='initial')
]