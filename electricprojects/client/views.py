from re import sub as regular_substituition

from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .forms import formDataClient, formAddress
from main.models import a11City, a12District
from .models import b01Clients, b02Address


def get_next_id(table):
    try:
        new_id = table.objects.latest('id').id + 1
    except ObjectDoesNotExist:
        new_id = 1
    return new_id


def initial(request):
    if request.method == "GET":
        return render(request, "client/initial.html")
    else:
        return HttpResponse(status=405)


def add_client(request):
    if request.method == "GET":
        return render(request, "client/add-client.html", {
            "formAddClient": formDataClient()})
    elif request.method == "POST":
        form = formDataClient(request.POST)
        if form.is_valid():
            try:
                id_client = b01Clients.objects.latest('id').id + 1
            except ObjectDoesNotExist:
                id_client = 1
            if form.cleaned_data['fone'] != '' or form.cleaned_data['fone'] != '0':
                fone = regular_substituition(r"\D", "", form.cleaned_data['fone'])
            else:
                fone = ''
            new_client = b01Clients(
                id=id_client,
                treatment=form.cleaned_data['treatment'],
                name=form.cleaned_data['name'],
                cnpj=form.cleaned_data['cnpj'],
                description=form.cleaned_data['description'],
                fone=fone,
                email=form.cleaned_data['email'],
            )
            new_client.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)


def edit_client_information(request, id_client):
    if request.method == "GET":
        client = b01Clients.objects.get(id=id_client)
        return render(request, "client/edit-client.html", {"client": client})
    elif request.method == "POST":
        form = formDataClient(request.POST)
        if form.is_valid():
            if form.cleaned_data['fone'] != '' or form.cleaned_data['fone'] != '0':
                fone = regular_substituition(r"\D", "", form.cleaned_data['fone'])
            else:
                fone = ''
            client = b01Clients.objects.get(id=id_client)
            client.treatment = form.cleaned_data['treatment']
            client.name = form.cleaned_data['name']
            client.cnpj = form.cleaned_data['cnpj']
            client.description = form.cleaned_data['description']
            client.fone = fone
            client.email = form.cleaned_data['email']
            client.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)


def select_client(request):
    if request.method == "GET":
        clients = b01Clients.objects.all().only('id', 'description').order_by('description')
        return render(request, "client/select-client.html", {'clients': clients})
    elif request.method == "POST":
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)


def new_address(request, id_client):
    if request.method == "GET":
        client = b01Clients.objects.get(id=id_client)
        return render(request, "client/new-address.html", {
            "form": formAddress(), "client": client})
    elif request.method == "POST":
        form = formAddress(request.POST)
        if form.is_valid():
            if form.cleaned_data['new_district'] != '':
                id_new_district = get_next_id(a12District)
                new_district = a12District(
                    id=id_new_district,
                    description=form.cleaned_data['new_district'],
                    city=form.cleaned_data['city']
                )
                new_district.save()
                district = new_district
            elif form.cleaned_data['district'] != '':
                district = form.cleaned_data['district']
            else:
                return HttpResponse(status=400)
            new_address = b02Address(
                id=get_next_id(b02Address),
                client_id=id_client,
                district=district,
                street=form.cleaned_data['street'],
                complement=form.cleaned_data['complement']
            )
            new_address.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)


def ajax_load_cities(request, id_state):
    if request.method == "GET":
        cities = a11City.objects.filter(state_id=id_state)
        return render(request, "client/ajax-load-cities.html", {
            "cities": cities})
    else:
        return HttpResponse(status=405)

def ajax_load_districts(request, id_city):
    if request.method == "GET":
        districts = a12District.objects.filter(city_id=id_city)
        return render(request, "client/ajax-load-districts.html", {
            "districts": districts})
    else:
        return HttpResponse(status=405)


def ajax_load_address_client(request, id_client):
    if request.method == "GET":
        raw_query_address = """
                SELECT client_b02address.id, client_b02address.street, client_b02address.complement,
                main_a12district.description as district_description, main_a11city.description as city, 
                main_a10state.uf as state
                FROM client_b02address
                INNER JOIN main_a12district ON client_b02address.district_id = main_a12district.id
                INNER JOIN main_a11city ON main_a12district.city_id = main_a11city.id
                INNER JOIN main_a10state ON main_a11city.state_id = main_a10state.id
                WHERE client_b02address.client_id = %s
                ORDER BY client_b02address.id
            """
        addresses = b02Address.objects.raw(raw_query_address, [id_client])
        for address in addresses:
            address.description = f"{address.city}-{address.state}, {address.district_description}, {address.street}, {address.complement}"
        return render(request, "client/ajax-load-address-client.html", {
            "addresses": addresses
        })
    else:
        return HttpResponse(status=405)
