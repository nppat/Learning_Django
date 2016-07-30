"""multiple_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include # include include
# from django.contrib import admin # don't need admin

urlpatterns = [
    url(r'^', include("apps.multiple.urls")), # this main project, multiple_apps
    url(r'^main/', include("apps.first_app.urls")),
    url(r'^ninja_gold/', include("apps.gold.urls")),
    url(r'^ninjas', include("apps.turtles.urls")),
    url(r'^logreg/', include("apps.login.urls")),
    url(r'^courses/', include("apps.courses.urls")),

]