# from django.db import models
from django.contrib.gis.db import models


class ZoneType(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class InterestZone(models.Model):
    name = models.CharField(max_length=255)
    zone_type = models.ForeignKey(ZoneType)
    acquisition_date = models.DateTimeField(
        'DateAdded', auto_now=True, auto_now_add=False)
    geometry = models.PolygonField(
        srid=4326, null=True, blank=True, help_text='Area')

    objects = models.GeoManager()

    class Meta:
        verbose_name = ('Interest Zone')
        verbose_name_plural = ('Interest Zones')
        ordering = ('acquisition_date', 'name')

