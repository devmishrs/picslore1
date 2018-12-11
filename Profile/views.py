from django.shortcuts import render, redirect
from Profile.forms import ProfView, editProfileChangeForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.views.generic import View
from Profile.forms import *
from django.http import HttpResponse

# Create your views here.

def home(request):
    # form = ProfView(request.POST)
    context = {'user':request.user}
    return render(request,'accounts/home.html', context)

def edit_prof(request):
    if request.method == 'POST':
        form = editProfileChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = editProfileChangeForm(instance = request.user)
        context = {
            'form':form
        }
        return render(request, 'accounts/edit_prof.html',context)

def change_password(request):
    if request.method==['POST']:
        form = PasswordChangeForm(request.POST, user = request.user)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PasswordChangeForm(user = request.user)
        context = {
            'form':form
        }
        return render(request, 'accounts/change_password.html', context)


class getAddress(View):
    def get(self, request):
        addressForm = AddressForm(request.GET)
        if addressForm.is_valid():
            addressForm.save()
            print('Im calling this')
            #return render('accounts/home.html',{'add_form': addressForm})
            return HttpResponse('adds')
            
        

    



