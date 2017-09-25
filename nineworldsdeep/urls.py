"""nineworldsdeep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import core.views

urlpatterns = [
	#url(r'^$', core.views.index, name='index'), 
	#url(r'^$', TemplateView.as_view(template_name="bootstrap-index.html")),
	url(r'^$', core.views.index, name='index'),
	url(r'^sandbox/', TemplateView.as_view(template_name="bootstrap-index.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^documents/$', core.views.DocumentListView.as_view(), name='documents'),
    url(r'^documents/(?P<pk>\d+)$', core.views.DocumentDetailView.as_view(), name='document-detail'),
]
