from django import forms
from .models import UserProfile
from accounts.models import User
from django.contrib.auth.forms import UserChangeForm

class ProfView(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
        )
        labels = {
            'username' : 'Username',
            'first_name' : 'First Name',
            'last_name' :'Last Name',
            'email' :'Email',
            'phone_number' :'Phone Number',
        }

    profile_pic = forms.ImageField(label = "Profile Photo")
    address = forms.CharField(label = 'Address')
    city = forms.CharField(label = 'City', max_length= 300)
    state = forms.CharField(label = 'State', max_length=33)
    country = forms.CharField(label = 'Country', max_length=33)

    def get_fullname(request):
        return request.get_full_name()


class editProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
    

