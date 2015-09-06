
# def homepage(request):
#     location = get_location(request)

#     return render_to_response('homepage.html', {'user': request.user, 'lat_lng': location['lat_lng'],
#                                                 'city': location['city'], 'state_abbr': location['state_abbr']},
#                               context_instance=RequestContext(request))

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
# from django.views.generic import View

# from .models import Effort

# # Create your views here.

# # def index(request):
# #     latest_route_list = Route.objects.order_by('-created_at')[:5]
# #     output = ', '.join([r.location for r in latest_route_list])
# #     return HttpResponse(output)

# def index(request):
#     latest_effort_list = Effort.objects.order_by('-created_at')[:5]
#     template = loader.get_template('efforts/index.html')
#     context = RequestContext(request, {
#         'latest_effort_list': latest_effort_list,
#     })
#     return HttpResponse(template.render(context))

# def detail(request, effort_id):
#     return HttpResponse("Effort #%s." % effort_id)

def homepage(request):
    # template = loader.get_template('django_rundeck/templates/django_rundeck/homepage.html')
    # context = RequestContext(request, {

    # })
    # return HttpResponse(template.render(context))
    # return render_to_response('efforts/homepage.html')
    return render_to_response('django_rundeck/homepage.html')
