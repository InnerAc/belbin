"""belbins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'belbin.views.index' , name='index'),
    url(r'^match$', 'belbin.match.match' , name='match'),
    url(r'^register/', 'belbin.views.register', name='register'),
    url(r'^exam/', 'belbin.views.exam', name='exam'),
    url(r'^info/(.+)', 'belbin.views.info', name='info'),
    url(r'^logout', 'belbin.views.logout', name='logout'),
    
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),  
]
