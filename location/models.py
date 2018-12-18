from django.db import models
from django.contrib.gis.db import models as gis_model
from django.db.models import Manager as GeoManager


# Create your models here.
class PlaceMap(models.Model):
    name = models.CharField(max_length=66)
    location = gis_model.PointField(
            srid=4326,
            null=True,
            spatial_index=True,
            geography=True)
        
    objects = GeoManager()


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'PlaceMap'


class Places(models.Model):
    osm_id = models.BigIntegerField()
    name = models.CharField(max_length=48)
    type = models.CharField(max_length=16)
    population = models.BigIntegerField()
    geom = gis_model.MultiPointField(srid=4326)

    def __str__(self):
        return self.name

