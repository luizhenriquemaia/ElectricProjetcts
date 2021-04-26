from django.urls import path

from . import views


app_name = "client"

urlpatterns = [
    path('<int:id_client>/', views.edit_client_information, name='edit_client_information'),
    path('add-client/', views.add_client, name='add_client'),
    path('<int:id_client>/new-address/', views.new_address, name='new_address'),
    path('select-client/', views.select_client, name='select_client'),
    path('ajax/possible-clients/', views.initial, name='initial'),
    path('ajax/load-cities/<int:id_state>', views.ajax_load_cities, name='ajax_load_cities'),
    path('ajax/load-districts/<int:id_city>', views.ajax_load_districts, name='ajax_load_districts'),
    path('ajax/load-addresses/<int:id_client>', views.ajax_load_address_client, name='ajax_load_address_client'),
]