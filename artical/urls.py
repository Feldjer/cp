from django.conf.urls import url, include
from django.contrib import admin
from artical import views

admin.autodiscover()

urlpatterns = [
    url(r'^list/', views.list, name='list'),
	url(r'^$', views.home, name='home'),
    url(r'^article/$', views.article, name='article'),
]
