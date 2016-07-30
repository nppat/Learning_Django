from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # root route
    url(r'products/show/(?P<id>\d+)$', views.show), # show
    url(r'products/new$', views.new),	# new route
    url(r'products/(?P<id>\d+)/edit$', views.edit), # edit route
    url(r'products$', views.create), # create route
    url(r'products/update/(?P<id>\d+)$', views.update), # update route
    url(r'products/destroy/(?P<id>\d+)$', views.destroy), # destroy route
]
