from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic import View
from django.contrib.gis.geos import Point
from location.models import *

class GetLocationData(View):
    @csrf_exempt
    def post(self, request):
        print('AJAX CALLED!!')
        if request.is_ajax():
            lat = request.POST['latitude']
            long = request.POST['longitude']
            print(type(lat)) 
            print(long)
            lat=float(lat)
            long=float(long)
            n = Point(lat,long)
            print(n) 
            print('Location View is called.');
           

        #print(request.POST['longitude'])
        return HttpResponse('Hi')
'''
    def get(self, request):
        return HttpResponse('hello')
    
'''
