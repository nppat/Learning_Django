from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # set up index route
    url(r'^survey/process', views.process), # survey/process route
    url(r'^result', views.result), # result route
    url(r'^survey/go_back', views.index) # survey/go_back, return to index.html
]
