from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserLoginForm, HomeViewNew
#from .forms import UserLoginForm, UserAdminCreationForm, UserAdminChangeForm, RegistrationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.views.generic import ListView


def loginn(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_obj = form.cleaned_data.get('user_obj')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request ,'accounts/login.html', {'form' : form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data('username')
            # raw_password = form.cleaned_data('password')
            #'us':us user = authenticate(username =username, password = raw_password)
            # login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})




# def home(request):

#     if request.method == 'GET':
#         form = HomeViewNew()
#         args = { 
#             'form':form,
#         }
            
#     return render(request, 'accounts/home.html', args)

def logout_view(request):
    logout(request)
    return redirect('login')
    #return HttpResponseRedirect(re)

class SearchView(ListView):
    pass
