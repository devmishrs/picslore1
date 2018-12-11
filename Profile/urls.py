from Profile.views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^set_address/$',getAddress.as_view(), name = 'GetAddress'),
]