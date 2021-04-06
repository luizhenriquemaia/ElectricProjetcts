from csv import reader
from io import StringIO
from pathlib import Path

from django.http import HttpResponse
from django.shortcuts import render

from main.models import (a01MethodsRef, a02MethodsInst, a03IsolationType,
                     a04NumberOfChargedConductors, a05CurrentCapacity,
                     a06TemperatureCorrection, a07UndergroundCorrection,
                     a08GroupingForms, a09GroupingCorrection)


def config_options(request):
    if request.method == "GET":
        return render(request, "config/initial.html")
    else:
        return HttpResponse(status=405)


def reference_methods(request):
    if request.method == "GET":
        reference_methods = a01MethodsRef.objects.all().order_by('id')
        return render(request, "config/reference-methods.html", {
            "referenceMethods": reference_methods})
    else:
        return HttpResponse(status=405)


def ajax_add_basic_data_a01(request):
    if request.method == "GET":
        if a01MethodsRef.objects.all().exists():
            return HttpResponse(status=400)
        else:
            csv_file = Path.cwd().joinpath("seeds_db", 'a01MethodsRef.csv')
            data_set = csv_file.read_text(encoding='UTF-8')
            io_string = StringIO(data_set)
            for count, column in enumerate(reader(io_string, delimiter=';', quotechar='|')):
                new_method = a01MethodsRef(
                    id=count+1,
                    reference=column[0].strip(' "'),
                    description=column[1].strip(' "')
                )
                new_method.save()
            return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)


def ajax_list_reference_methods(request):
    if request.method == "GET":
        reference_methods = a01MethodsRef.objects.all().order_by('id')
        return render(request, "config/ajax-load-reference-methods.html", {
            "referenceMethods": reference_methods})
    else:
        return HttpResponse(status=405)

def instalation_methods(request):
    if request.method == "GET":
        instalation_methods = a02MethodsInst.objects.all().order_by('id')
        return render(request, "config/instalation-methods.html", {
            "instalationMethods": instalation_methods})
    else:
        return HttpResponse(status=405)

def ajax_add_basic_data_a02(request):
    if request.method == "GET":
        if a02MethodsInst.objects.all().exists():
            return HttpResponse(status=400)
        else:
            csv_file = Path.cwd().joinpath("seeds_db", 'a02MethodsInst.csv')
            data_set = csv_file.read_text(encoding='UTF-8')
            io_string = StringIO(data_set)
            for count, column in enumerate(reader(io_string, delimiter=';', quotechar='|')):
                maximum_diameter = 0 if column[3].strip(' "') == '' else column[3].strip(' "')
                new_method = a02MethodsInst(
                    id=count+1,
                    method=column[0].strip(' "'),
                    description=column[1].strip(' "'),
                    reference_method_id=column[2].strip(' "'),
                    maximum_diameter=maximum_diameter,
                    cable_type=column[4].strip(' "'),
                )
                new_method.save()
            return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)

def ajax_list_instalation_methods(request):
    if request.method == "GET":
        instalation_methods = a02MethodsInst.objects.all().order_by('id')
        return render(request, "config/ajax-load-instalation-methods.html", {
            "instalationMethods": instalation_methods})
    else:
        return HttpResponse(status=405)

def isolation_types(request):
    if request.method == "GET":
        isolation_types = a03IsolationType.objects.all().order_by('id')
        return render(request, "config/isolation-types.html", {
            "isolationTypes": isolation_types})
    else:
        return HttpResponse(status=405)

def ajax_add_basic_data_a03(request):
    if request.method == "GET":
        if a03IsolationType.objects.all().exists():
            return HttpResponse(status=400)
        else:
            csv_file = Path.cwd().joinpath("seeds_db", 'a03IsolationType.csv')
            data_set = csv_file.read_text(encoding='UTF-8')
            io_string = StringIO(data_set)
            for count, column in enumerate(reader(io_string, delimiter=';', quotechar='|')):
                new_isolation = a03IsolationType(
                    id=count+1,
                    description=column[0].strip(' "'),
                    max_temperature=column[1].strip(' "'),
                    overload_temperature=column[2].strip(' "'),
                    short_circuit_temperature=column[3].strip(' "'),
                )
                new_isolation.save()
            return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)

def ajax_list_isolation_types(request):
    if request.method == "GET":
        isolation_types = a03IsolationType.objects.all().order_by('id')
        return render(request, "config/ajax-load-isolation-types.html", {
            "isolationTypes": isolation_types})
    else:
        return HttpResponse(status=405)

def charged_conductors(request):
    if request.method == "GET":
        charged_conductors = a04NumberOfChargedConductors.objects.all().order_by('id')
        return render(request, "config/charged-conductors.html", {
            "chargedConductors": charged_conductors})
    else:
        return HttpResponse(status=405)

def ajax_add_basic_data_a04(request):
    if request.method == "GET":
        if a04NumberOfChargedConductors.objects.all().exists():
            return HttpResponse(status=400)
        else:
            csv_file = Path.cwd().joinpath("seeds_db", 'a04NumberOfChargedConductors.csv')
            data_set = csv_file.read_text(encoding='UTF-8')
            io_string = StringIO(data_set)
            for count, column in enumerate(reader(io_string, delimiter=';', quotechar='|')):
                new_number = a04NumberOfChargedConductors(
                    id=count+1,
                    circuit_esqueme=column[0].strip(' "'),
                    number=column[1].strip(' "')
                )
                new_number.save()
            return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)

def ajax_list_charged_conductors(request):
    if request.method == "GET":
        charged_conductors = a04NumberOfChargedConductors.objects.all().order_by('id')
        return render(request, "config/ajax-load-charged-conductors.html", {
            "chargedConductors": charged_conductors})
    else:
        return HttpResponse(status=405)

def current_capacities(request):
    if request.method == "GET":
        current_capacities = a05CurrentCapacity.objects.all().order_by('id')
        return render(request, "config/current-capacities.html", {
            "currentCapacities": current_capacities})
    else:
        return HttpResponse(status=405)

def ajax_add_basic_data_a05(request):
    if request.method == "GET":
        if a05CurrentCapacity.objects.all().exists():
            return HttpResponse(status=400)
        else:
            csv_file = Path.cwd().joinpath("seeds_db", 'a05CurrentCapacity.csv')
            data_set = csv_file.read_text(encoding='UTF-8')
            io_string = StringIO(data_set)
            for count, column in enumerate(reader(io_string, delimiter=';', quotechar='|')):
                new_current_capacity = a05CurrentCapacity(
                    id=count+1,
                    nominal_section=column[0].strip(' "'),
                    reference_method_id=column[1].strip(' "'),
                    number_of_charged_conductors=column[2].strip(' "'),
                    cable_type=column[3].strip(' "'),
                    capacity=column[4].strip(' "'),
                    isolation_type_id=column[5].strip(' "'),
                )
                new_current_capacity.save()
            return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)

def ajax_list_current_capacities(request):
    if request.method == "GET":
        current_capacities = a05CurrentCapacity.objects.all().order_by('id')
        return render(request, "config/ajax-load-current-capacities.html", {
            "currentCapacities": current_capacities})
    else:
        return HttpResponse(status=405)

def temperature_corrections(request):
    if request.method == "GET":
        temperature_corrections = a06TemperatureCorrection.objects.all().order_by('id')
        return render(request, "config/temperature-corrections.html", {
            "temperatureCorrections": temperature_corrections})
    else:
        return HttpResponse(status=405)

def ajax_add_basic_data_a06(request):
    if request.method == "GET":
        if a06TemperatureCorrection.objects.filter(id=1).exists():
            return HttpResponse(status=400)
        else:
            csv_file = Path.cwd().joinpath("seeds_db", 'a06TemperatureCorrection.csv')
            data_set = csv_file.read_text(encoding='UTF-8')
            io_string = StringIO(data_set)
            for count, column in enumerate(reader(io_string, delimiter=';', quotechar='|')):
                new_temperature_correction = a06TemperatureCorrection(
                    id=count+1,
                    location=column[0].strip(' "'),
                    temperature=column[1].strip(' "'),
                    isolation_type_id=column[2].strip(' "'),
                    factor=column[3].strip(' "'),
                )
                new_temperature_correction.save()
            return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)

def ajax_list_temperature_corrections(request):
    if request.method == "GET":
        temperature_corrections = a06TemperatureCorrection.objects.all().order_by('id')
        return render(request, "config/ajax-load-temperature-corrections.html", {
            "temperatureCorrections": temperature_corrections})
    else:
        return HttpResponse(status=405)

def underground_corrections(request):
    if request.method == "GET":
        underground_corrections = a07UndergroundCorrection.objects.all().order_by('id')
        return render(request, "config/underground-corrections.html", {
            "undergroundCorrections": underground_corrections})
    else:
        return HttpResponse(status=405)

def ajax_add_basic_data_a07(request):
    if request.method == "GET":
        if a07UndergroundCorrection.objects.all().exists():
            return HttpResponse(status=400)
        else:
            csv_file = Path.cwd().joinpath("seeds_db", 'a07UndergroundCorrection.csv')
            data_set = csv_file.read_text(encoding='UTF-8')
            io_string = StringIO(data_set)
            for count, column in enumerate(reader(io_string, delimiter=';', quotechar='|')):
                new_underground_correction = a07UndergroundCorrection(
                    id=count+1,
                    thermal_resistivity=column[0].strip(' "'),
                    correction_factory=column[1].strip(' "'),
                )
                new_underground_correction.save()
            return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)

def ajax_list_underground_corrections(request):
    if request.method == "GET":
        underground_corrections = a07UndergroundCorrection.objects.all().order_by('id')
        return render(request, "config/ajax-load-underground-corrections.html", {
            "undergroundCorrections": underground_corrections})
    else:
        return HttpResponse(status=405)

def grouping_forms(request):
    if request.method == "GET":
        grouping_forms = a08GroupingForms.objects.all().order_by('id')
        return render(request, "config/grouping-forms.html", {
            "groupingForms": grouping_forms})
    else:
        return HttpResponse(status=405)

def ajax_add_basic_data_a08(request):
    if request.method == "GET":
        if a08GroupingForms.objects.all().exists():
            return HttpResponse(status=400)
        else:
            csv_file = Path.cwd().joinpath("seeds_db", 'a08GroupingForms.csv')
            data_set = csv_file.read_text(encoding='UTF-8')
            io_string = StringIO(data_set)
            for count, column in enumerate(reader(io_string, delimiter=';', quotechar='|')):
                new_group = a08GroupingForms(
                    id=count+1,
                    description=column[0].strip(' "'),
                    reference_method_id=column[1].strip(' "'),
                )
                new_group.save()
            return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)

def ajax_list_grouping_forms(request):
    if request.method == "GET":
        grouping_forms = a08GroupingForms.objects.all().order_by('id')
        return render(request, "config/ajax-load-grouping-forms.html", {
            "groupingForms": grouping_forms})
    else:
        return HttpResponse(status=405)


def grouping_corrections(request):
    if request.method == "GET":
        grouping_corrections = a09GroupingCorrection.objects.all().order_by('id')
        return render(request, "config/grouping-corrections.html", {
            "groupingCorrections": grouping_corrections})
    else:
        return HttpResponse(status=405)

def ajax_add_basic_data_a09(request):
    if request.method == "GET":
        if a09GroupingCorrection.objects.all().exists():
            return HttpResponse(status=400)
        else:
            csv_file = Path.cwd().joinpath("seeds_db", 'a09GroupingCorrection.csv')
            data_set = csv_file.read_text(encoding='UTF-8')
            io_string = StringIO(data_set)
            for count, column in enumerate(reader(io_string, delimiter=';', quotechar='|')):
                new_group_correction = a09GroupingCorrection(
                    id=count+1,
                    group_form_id=column[0].strip(' "'),
                    circuit_number=column[1].strip(' "'),
                    factor=column[2].strip(' "'),
                )
                new_group_correction.save()
            return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)

def ajax_list_grouping_corrections(request):
    if request.method == "GET":
        grouping_corrections = a09GroupingCorrection.objects.all().order_by('id')
        return render(request, "config/ajax-load-grouping-corrections.html", {
            "groupingCorrections": grouping_corrections})
    else:
        return HttpResponse(status=405)