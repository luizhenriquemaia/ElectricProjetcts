from django.http import HttpResponse
from django.shortcuts import render


def initial(request):
    if request.method == "GET":
        return render(request, "main/initial.html")
    else:
        return HttpResponse(status=405)

