from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .models import Route

def index(request):
    latest_route_list = Route.objects.order_by('-created_at')[:5]
    output = ', '.join([r.location for r in latest_route_list])
    return HttpResponse(output)

def detail(request, route_id):
    return HttpResponse("Route #%s." % route_id)

