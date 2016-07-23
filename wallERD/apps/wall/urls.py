from django.conf.urls import url
from . import views	# bring in all of views
urlpatterns = [
    url(r'^$', views.index), # root route to index.html
]
