from django.conf.urls import url
from . import views # bring in views

urlpatterns = [
    url(r'^$', views.index), # root route
    url(r'course/create$', views.create), # create course
    url(r'course/destroy/(?P<id>\d+)$', views.destroy), # remove course
]
