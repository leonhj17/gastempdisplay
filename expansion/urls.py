# _*_ encoding:utf-8 _*_
from django.conf.urls import url, include
from rest_framework import routers

from expansion import views


router = routers.DefaultRouter()
router.register(r'kks', views.KksViewset)
router.register(r'value', views.MeasureValueViewset)

# 此处（?P<>）格式标记参数名称
urlpatterns = [
    url(r'^f5/', views.f5_ajax, name='f5'),
    url(r'^query_vector', views.query_vector, name='query_vector'),
    url(r'^query_ab', views.query_ab, name='query_ab'),
    url(r'^funview/', views.funview),
    url(r'^addview/', views.addview, name='add'),
    url(r'^addview2/(\d+)/(\d+)', views.add_redirect),
    url(r'^new_add/(\d+)/(\d+)', views.addview2, name='add2'),
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
