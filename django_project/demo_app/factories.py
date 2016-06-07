__author__ = 'Christian Christelis <christian@kartoza.com>'
__date__ = '07/06/16'

import factory
from demo_app.models import ZoneType, InterestZone


class ZoneTypeFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "client_%d" % n)

    class Meta:
        model = ZoneType


class InterestZoneFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "client_%d" % n)
    zone_type = factory.SubFactory(
        'demo_app.factories.ZoneTypeFactory')
    # acquisition_date =
    # geometry =

    class Meta:
        model = InterestZone
