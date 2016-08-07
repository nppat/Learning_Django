from django.conf.urls import url
from . import views # bring in the views

urlpatterns = [
    url(r'^$', views.index), # index route
    url(r'friends/login$', views.login), # Login
    url(r'friends/register$', views.register), # Register
    url(r'friends/dashboard/$', views.dashboard), # Show user dashboard
    url(r'friends/user/(?P<id>\d+)$', views.user), # Show user profile page
    url(r'friends/add_friend/(?P<user_id>\d+)$', views.add_friend), # Add friend
    # url(r'friends/remove$', views.remove_friend), # Remove friend
    url(r'friends/logout$', views.logout) # Logout
]