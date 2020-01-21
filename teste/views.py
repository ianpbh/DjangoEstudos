from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request.GET)
    return HttpResponse("teste de response")


def template(request, nome = None):
    return render(request,"teste/template.html", {'nome':nome})
