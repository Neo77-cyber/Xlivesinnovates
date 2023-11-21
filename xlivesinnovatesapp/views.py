from django.shortcuts import render, redirect
from django.contrib.auth.models import  auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FishPondForm

# Create your views here.


def home(request):

    
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username = username, password= password)

            if user is not None:
                auth.login(request,user)
                return redirect('farmrecords')
            else:
                messages.info(request, 'Contact us on our social accounts below')
                return redirect('signin')

    
    return render(request, 'signin.html')

@login_required(login_url='home')
def farm_records(request):
    if request.method == 'POST':
        form = FishPondForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = FishPondForm()

    
    return render(request, 'farmrecords.html', {'form': form})

@login_required(login_url='home')
def success(request):

    
    return render(request, 'success.html')