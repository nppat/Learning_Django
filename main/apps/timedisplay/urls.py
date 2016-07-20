from django.conf.urls import url
from . import views # import all from views 

urlpatterns = [
    url(r'^$', views.index) # $ in regex will point to nothing
]