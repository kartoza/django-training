from django.conf.urls import patterns

urlpatterns = patterns('doodle_app.views',
    (r'helloWorld/$', 'helloWorld'),
    (r'menu/$', 'menu'),
    (r'hello/(?P<thePerson>[a-zA-Z]+)/$', 'hello'),
    (r'listDoodleTypes/$', 'listDoodleTypes'),
    (r'listDoodles/$', 'listDoodles'),
    (r'^showDoodleType/(?P<theId>\d+)/$', 'showDoodleType'),
    (r'^deleteDoodleType/(?P<theId>\d+)/$', 'deleteDoodleType'),
    (r'^createDoodleType/(?P<theName>[a-zA-Z]+)/$', 'createDoodleType'),
    (r'^updateDoodleType/(?P<theId>\d+)/(?P<theName>[a-zA-Z]+)/$',
       'updateDoodleType'),
    (r'^newDoodleForm/$', 'doodleForm'),
    (r'^doodleForm/(?P<theId>\d+)/$', 'doodleForm'),
)
