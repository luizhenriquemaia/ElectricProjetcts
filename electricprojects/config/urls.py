from django.urls import path

from . import views


app_name = "config"

urlpatterns = [
    path('', views.config_options, name='config_options'),
    path('reference-method/', views.reference_methods, name='reference_methods'),
    path('reference-method/ajax/add-a01/', views.ajax_add_basic_data_a01, name='ajax_add_basic_data_a01'),
    path('reference-method/ajax/list-reference-methods/', views.ajax_list_reference_methods, name='ajax_list_reference_methods'),
    path('instalation-method/', views.instalation_methods, name='instalation_methods'),
    path('instalation-method/ajax/add-a02/', views.ajax_add_basic_data_a02, name='ajax_add_basic_data_a02'),
    path('instalation-method/ajax/list-instalation-methods/', views.ajax_list_instalation_methods, name='ajax_list_instalation_methods'),
    path('isolation-type/', views.isolation_types, name='isolation_types'),
    path('isolation-type/ajax/add-a03/', views.ajax_add_basic_data_a03, name='ajax_add_basic_data_a03'),
    path('isolation-type/ajax/list-isolation-types/', views.ajax_list_isolation_types, name='ajax_list_isolation_types'), 
    path('charged-conductor/', views.charged_conductors, name='charged_conductors'),
    path('charged-conductor/ajax/add-a04/', views.ajax_add_basic_data_a04, name='ajax_add_basic_data_a04'),
    path('charged-conductor/ajax/list-charged-conductors/', views.ajax_list_charged_conductors, name='ajax_list_charged_conductors'),
    path('current-capacitie/', views.current_capacities, name='current_capacities'),
    path('current-capacitie/ajax/add-a05/', views.ajax_add_basic_data_a05, name='ajax_add_basic_data_a05'),
    path('current-capacitie/ajax/list-current-capacities/', views.ajax_list_current_capacities, name='ajax_list_current_capacities'),
    path('temperature-correction/', views.temperature_corrections, name='temperature_corrections'),
    path('temperature-correction/ajax/add-a06/', views.ajax_add_basic_data_a06, name='ajax_add_basic_data_a06'),
    path('temperature-correction/ajax/list-temperature-corrections/', views.ajax_list_temperature_corrections, name='ajax_list_temperature_corrections'),
    path('underground-correction/', views.underground_corrections, name='underground_corrections'),
    path('underground-correction/ajax/add-a07/', views.ajax_add_basic_data_a07, name='ajax_add_basic_data_a07'),
    path('underground-correction/ajax/list-underground-corrections/', views.ajax_list_underground_corrections, name='ajax_list_underground_corrections'),
    path('grouping-form/', views.grouping_forms, name='grouping_forms'),
    path('grouping-form/ajax/add-a08/', views.ajax_add_basic_data_a08, name='ajax_add_basic_data_a08'),
    path('grouping-form/ajax/list-grouping-forms/', views.ajax_list_grouping_forms, name='ajax_list_grouping_forms'),
    path('grouping-correction/', views.grouping_corrections, name='grouping_corrections'),
    path('grouping-correction/ajax/add-a09/', views.ajax_add_basic_data_a09, name='ajax_add_basic_data_a09'),
    path('grouping-correction/ajax/list-grouping-corrections/', views.ajax_list_grouping_corrections, name='ajax_list_grouping_corrections'),
]