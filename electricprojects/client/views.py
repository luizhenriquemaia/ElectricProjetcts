from re import sub as regular_substituition

from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .forms import formAddClient
from .models import b01Clients

def initial(request):
    if request.method == "GET":
        return render(request, "client/initial.html")
    else:
        return HttpResponse(status=405)


def add_client(request):
    if request.method == "GET":
        return render(request, "client/add-client.html", {
            "formAddClient": formAddClient()})
    elif request.method == "POST":
        form = formAddClient(request.POST)
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


def add_address(request):
    if request.method == "GET":
        return render(request, "client/add-client.html", {
            "formAddClient": formAddClient()})
    elif request.method == "POST":
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)