from django.conf.urls import url
from . import views
# Set up the routes
urlpatterns = [
    url(r'^$', views.index), # index route
    url(r'^submit$', views.rword)	#on form submit, take this route
]
