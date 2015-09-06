from django.conf.urls import url 

from . import views

urlpatterns = [
    # ex: /efforts/
    url(r'^$', views.index, name='index'),

    # ex: /efforts/5/
    url(r'^(?P<route_id>[0-9]+)/$', views.detail, name='detail'),
    
    # ex: /route/
    # url(r'^(route)/$', views.route, name='route'),
]