from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^addshow$', views.create),
    url(r'^show/(?P<show_id>[0-9]+)$', views.showdet),
	url(r'^show/(?P<show_id>[0-9]+)/edit$', views.showedit),
    url(r'^shows$', views.shows),
	url(r'^edit_show/(?P<show_id>[0-9]+)$', views.edit_show),
    url(r'^delete_show/(?P<show_id>[0-9]+)$', views.delete_show)
]