"""gastempdisplay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from xadmin.plugins import xversion
import xadmin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
    url(r'^index/', TemplateView.as_view(template_name='index.html'), name='homepage'),
    url(r'^siderbar/', TemplateView.as_view(template_name='gasmonitor.html'), name='siderbar'),
    url(r'^waterwall/', include('waterwall.urls', namespace='waterwall')),
    url(r'^expansion/', include('expansion.urls', namespace='expansion')),
    url(r'^bootstrap/', TemplateView.as_view(template_name='expansionbase.html'))
]
