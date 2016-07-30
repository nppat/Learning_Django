from django.conf.urls import url
from . import views # bring in views

urlpatterns = [
    url(r'^$', views.index), # root route
    url(r'^registration/process$', views.process), # process registration route
    url(r'^login$', views.login), # login route
    url(r'^success$', views.success), # success route
    url(r'^go_back$', views.go_back) # back button route
]
