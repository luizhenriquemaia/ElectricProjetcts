from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .forms import formNewProject
from .models import c01Project


def get_next_id(table):
    try:
        new_id = table.objects.latest('id').id + 1
    except ObjectDoesNotExist:
        new_id = 1
    return new_id


def new_project(request):
    if request.method == "GET":
        form = formNewProject()
        return render(request, "project/new-project.html", {'form': form})
    elif request.method == "POST":
        form = formNewProject(request.POST)
        if form.is_valid():
            new_project = c01Project(
                id=get_next_id(c01Project),
                client=form.cleaned_data['client'],
                address=form.cleaned_data['address'],
                description=form.cleaned_data['description'],
                observation=form.cleaned_data['observation']
            )
            new_project.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)