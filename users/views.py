from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required #to make sure a link is accesible only if you are logged in

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #into the db
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You can now Log in  ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required #to ensure only logged in users can see a view
def profile(request):
    return render(request,'users/profile.html')