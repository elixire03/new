from django.conf.urls import url
from firstApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard', views.main, name='dashboard'),
    url(r'^dashboard/add_employee/$', views.create_employee, name='create_employee'),

]