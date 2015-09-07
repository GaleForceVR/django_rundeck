from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.views.generic import View
from django.core.urlresolvers import reverse

from .models import Route

def index(request):
    latest_route_list = Route.objects.order_by('-created_at')[:5]
    # output = ', '.join([r.location for r in latest_route_list])
    template = loader.get_template('routes/index.html')
    context = RequestContext(request, {
        'latest_route_list': latest_route_list,
    })
    return HttpResponse(template.render(context))

# def index(request):
#     latest_effort_list = Effort.objects.order_by('-created_at')[:5]
#     template = loader.get_template('efforts/index.html')
#     context = RequestContext(request, {
#         'latest_effort_list': latest_effort_list,
#     })
#     return HttpResponse(template.render(context))

def detail(request, route_id):
    current_route = Route.objects.get(pk=route_id)
    template = loader.get_template('routes/detail.html')
    context = RequestContext(request, {
        'current_route': current_route,
    })
    return HttpResponse(template.render(context))


def edit(request, route_id):
    p = get_object_or_404(Route, pk=route_id)
    p.location = request.POST['location']
    p.distance = request.POST['distance']
    p.save()
    return HttpResponseRedirect(reverse('routes:detail', args=(p.id,)))
