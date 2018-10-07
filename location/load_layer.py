import os
from django.contrib.gis.utils import LayerMapping
from .models import Places

places_mapping = {
    'osm_id': 'osm_id',
    'name': 'name',
    'type': 'type',
    'population': 'population',
    'geom': 'MULTIPOINT',
}

place_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'shape/places.shp'))

def run(verbose = True):
    lm =LayerMapping(Places, place_shp, places_mapping, transform= False, encoding='iso-8859-01')
    lm.save(strict=True, verbose= verbose)