from django.conf.urls import patterns

urlpatterns = patterns('doodle_app.views',
    (r'helloWorld/$', 'helloWorld'),
    (r'hello/(?P<thePerson>[a-zA-Z]+)/$', 'hello'),
    (r'listDoodleTypes/$', 'listDoodleTypes'),
    (r'^showDoodleType/(?P<theId>\d+)/$', 'showDoodleType'),
)
