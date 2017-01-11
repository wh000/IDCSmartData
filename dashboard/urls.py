from django.conf.urls import url

from . import views

app_name = 'dashboard'
urlpatterns = [
	url(r'^(?P<location>[a-zA-Z0-9]+)', views.location_info, name='location_info'),
    url(r'^.*$', views.home, name='home'),
]