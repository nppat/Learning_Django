from django.conf.urls import url
from . import views # bring in views

urlpatterns = [
    url(r'^$', views.index), # root route
    url(r'emails/submit$', views.submit), # submit, vaidate, return response route
]
