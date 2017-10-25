# _*_ encoding:utf-8 _*_
from django.conf.urls import url

from expansion import views

# 此处（?P<>）格式标记参数名称
urlpatterns = [
    url(r'^funview/', views.funview),
    url(r'^addview/', views.addview, name='add'),
    url(r'^addview2/(\d+)/(\d+)', views.add_redirect),
    url(r'^new_add/(\d+)/(\d+)', views.addview2, name='add2')
]
