__author__ = 'Christian Christelis <christian@kartoza.com>'
__date__ = '06/06/16'

from rest_framework import serializers

from demo_app.models import InterestZone

class InterestZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterestZone
        fields = ('name', 'zone_type', 'acquisition_date', 'geometry')
