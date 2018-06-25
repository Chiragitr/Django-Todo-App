
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index/$', views.index, name="index"),
    url(r'add/$', views.addtodo, name="add"),
    url(r'complete/(?P<id>[0-9]+)$', views.completeTodo, name="complete"),
    url(r'deleteall/$', views.deleteall, name="deleteall"),
    url(r'deletecompleted/$', views.deletecompleted, name="deletecompleted")
]
