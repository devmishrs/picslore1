from django.urls import path, re_path
from .views import signup, loginn, logout_view
from Profile.views import home, edit_prof, change_password          ## Imported From Profile app 
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from location.views import GetLocationData 

urlpatterns = [
    re_path(r'^$', home, name='home'),
    re_path(r'^edit_prof$', edit_prof, name='edit_profile'),
    re_path(r'^change_password', change_password, name='change_password'),


    re_path(r'^signup/$', signup, name='signup'),
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^get_location/$', GetLocationData.as_view(), name='getLocation'),
]
