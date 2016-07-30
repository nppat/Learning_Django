from django.conf.urls import url
from . import views # import your views!

urlpatterns = [
    url(r'^$', views.index), # root route
   	url(r'ninja/$', views.show), # show all TMNT
   	url(r'ninja/(?P<color>\w*)/$', views.show) # show individual TMNT using a regex \w* captures all word characters
]