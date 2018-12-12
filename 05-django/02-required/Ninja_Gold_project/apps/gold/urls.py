from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'process_money/(?P<location>\w+)$', views.process_money, name="process_money"),
    url(r'restart/$', views.destroy, name="destroy")
]