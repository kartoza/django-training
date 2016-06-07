from django.conf.urls import patterns, url

from demo_app.views import (
    LandingPage, AddZoneView)

from demo_app.api_views import zone_detail

urlpatterns = patterns(
    '',
    url(r'^$', LandingPage.as_view(), name='home'),
    url(r'^add-zone/$', AddZoneView.as_view(), name='add_zone'),
    url(r'^api/zone/(?P<pk>[0-9]+)$', zone_detail, name='zone_detail'),
)
