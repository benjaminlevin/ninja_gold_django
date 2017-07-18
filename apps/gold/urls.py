from django.conf.urls import url
from . import views           # This line is new!

#models -- views -- templates

urlpatterns = [
  url(r'^$', views.index), 
  url(r'^reset$', views.reset),
  url(r'^farm$', views.farm),
  url(r'^cave$', views.cave), 
  url(r'^house$', views.house),
  url(r'^casino$', views.casino),
  url(r'^process_money$', views.processMoney),      # This line has changed!
 ]