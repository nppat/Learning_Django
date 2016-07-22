from django.conf.urls import url
from . import views # brint in all from views

urlpatterns = [
    url(r'^$', views.index), # root route
    url(r'process_gold', views.process_gold), # process route
    url(r'reset', views.reset) # reset route
]
