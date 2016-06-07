__author__ = 'Christian Christelis <christian@kartoza.com>'
__date__ = '06/06/16'

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
