from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def index(request):
    return HttpResponse('Effort Index')

def detail(request, effort_id):
    return HttpResponse("Effort #%s." % effort_id)

# def route(request, route_id):
#     return HttpResponse("Route #%s." % route_id)

class Route(View):
    def get(self, request):
        return HTTPResponse('This is crazy')