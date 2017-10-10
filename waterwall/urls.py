# _*_ encoding:utf-8 _*_
from django.conf.urls import url
from .views import ExpansionView

urlpatterns = [
    url(r'^expansion/', ExpansionView.as_view(), name='expansion'),
]
