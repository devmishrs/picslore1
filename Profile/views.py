from django.shortcuts import render, redirect
from Profile.forms import ProfView, editProfileChangeForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

# Create your views here.

def home(request):
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



