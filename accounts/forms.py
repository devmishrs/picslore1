from django import forms
from .models import User
from django.forms import ModelForm
from django.db.models import Q
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Conformation', widget=forms.PasswordInput)
    
    class Meta(forms.ModelForm):
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match.")
        return password2

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
      #  user.username = self.cleaned_data['username']
       # user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get(' username')
        password = self.cleaned_data.get(' password')
        user_check = User.objects.filter(
            Q(username__iexact=username)|
            Q(email__iexact=username)
        ).distinct()
        if not user_check.exists() and user_check.count() != 1:
            raise forms.ValidationError('User does not exist.')
        user_obj = user_check.first()
        if not user_obj.check_password('password'):
            raise forms.ValidationError("Authentication is not correct!")
        self.cleaned_data['user_obj']
        return super(UserLoginForm, self).clean(*args, **kwargs)


class HomeViewNew(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
        )
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
        }



    
