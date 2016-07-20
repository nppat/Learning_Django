from django.conf.urls import url
from . import views # this line is new

urlpatterns = [
  url(r'^$', views.index) # this line changed
]