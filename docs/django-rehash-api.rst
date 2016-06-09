API
===

Making websites machine interpretable is a big benefit. This allows the
data to be used interesting ways than initially imagined. Another benefit
of creating an api is that internal applications can receive data
asynchronously. At this point our landing page should start feeling the strain
of all the interest zones.

Django rest framework
---------------------

Having a REST API is a benefit to both server and client and neither need to
consider the state of a request.

The django rest framework is the default app to include for this functionality.

If we wish to use this app to create a rest api, we need to include::

       'rest_framework',
       'rest_framework_gis',

in our installed apps.

Furthermore we need to create a api view and a serializer.

Our serializer could look as simple as::

	from rest_framework import serializers
	from demo_app.models import InterestZone
	class InterestZoneSerializer(serializers.ModelSerializer):

		class Meta:
			model = InterestZone # we are basing this very strongly on the model
			fields = ('name', 'zone_type', 'acquisition_date', 'geometry')



Our view itself would be more complicated, since we are allowing various
types of requests::

	from rest_framework import status
	from rest_framework.decorators import api_view
	from rest_framework.response import Response

	from demo_app.models import InterestZone
	from demo_app.serializers import InterestZoneSerializer


	@api_view(['GET', 'PUT', 'DELETE'])
	def zone_detail(request, pk):
		"""
		Get, udpate, or delete a specific zone
		"""
		try:
			zone = InterestZone.objects.get(pk=pk)
		except InterestZone.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if request.method == 'GET':
			serializer = InterestZoneSerializer(zone)
			return Response(serializer.data)

		elif request.method == 'PUT':
			serializer = InterestZoneSerializer(zone, data=request.DATA)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			else:
				return Response(
					InterestZoneSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

		elif request.method == 'DELETE':
			zone.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)


Lastly we need to connect this up to a url endpoint::

    url(r'^api/zone/(?P<pk>[0-9]+)$', zone_detail, name='zone_detail'),


Now we are able to view individual zones on the api.

Exercise
--------

Add functionality to view all zones and hook that up to the landing page,
to make the data load asynchronously.

