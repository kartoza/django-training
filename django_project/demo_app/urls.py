from django.conf.urls import patterns, url

from demo_app.views import (
    LandingPage, AddZoneView, AllRequestTypes,
    ToLandingPage
)

urlpatterns = patterns(
    '',
    url(r'^$', LandingPage.as_view(), name="index"),
    url(r'^index/$', ToLandingPage.as_view()),
    url(r'^request-types/$', AllRequestTypes.as_view(), name='request_Types'),
    url(r'^add-zone/$', AddZoneView.as_view(), name='add_zone'),
)
