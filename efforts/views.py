from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import View

from .models import Effort

# Create your views here.

# def index(request):
#     latest_route_list = Route.objects.order_by('-created_at')[:5]
#     output = ', '.join([r.location for r in latest_route_list])
#     return HttpResponse(output)

def index(request):
    latest_effort_list = Effort.objects.order_by('-created_at')[:5]
    template = loader.get_template('efforts/index.html')
    context = RequestContext(request, {
        'latest_effort_list': latest_effort_list,
    })
    return HttpResponse(template.render(context))

def detail(request, effort_id):
    return HttpResponse("Effort #%s." % effort_id)

# def route(request, route_id):
#     return HttpResponse("Route #%s." % route_id)

# class Route(View):
#     def get(self, request):
#         return HTTPResponse('This is crazy')