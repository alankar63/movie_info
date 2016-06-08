from django.conf.urls import url

from . import views 

urlpatterns = [
    url(r'^$', views.hello, name='test'),
    url(r'^([a-z0-9 ]+)/$',views.index,name="index"),
    
]

