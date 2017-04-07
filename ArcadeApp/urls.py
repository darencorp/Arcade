from django.conf.urls import include, url
from django.contrib import admin

from arcade import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^template/', views.template, name='template')
]
