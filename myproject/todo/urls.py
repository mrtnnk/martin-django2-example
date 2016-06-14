from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^(?P<pk>\d+)/edit$', views.edit, name='edit'),
    url(r'^(?P<pk>\d+)/done$', views.done, name='done'),
]
