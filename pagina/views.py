from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import PlanSolid, PlanPremium
from django.db import IntegrityError

# Create your views here.

def index(request):
    return render(request, 'index.html')

def wiki(request):
    return render(request, 'Info/wiki.html')

def plans(request):
    return render(request, 'profile/plans.html')

def requeriments(request):
    return render(request, 'Info/requeriments.html')

def download(request):
    return render(request, 'downloads.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'profile/signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
                user.save()
                login(request, user)
                return redirect('profile')
            except IntegrityError:
                return render(request, 'profile/signup.html', {'error': 'User already exist'})
        return render(request, 'index.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'profile/signin.html')
    else:
        user = authenticate(request,username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'profile/signin.html', {'error': 'User or password are incorrect'})
        else:
            login(request, user)
            return redirect('profile')

def work(request):
    return render(request,'Info/Working.html')


@login_required
def errorplan(request):
    return render(request,'profile/error-plan.html')

@login_required
def buy(request):
    planS = PlanSolid.objects.filter(user=request.user) 
    if planS.exists(): 
        return redirect('error-plan')
    else:
        if request.method == 'GET':
            return render(request, 'profile/buy.html')
        else:
            buy = PlanSolid(user=request.user,card=request.POST['card'],buyTime=timezone.now())
            buy.save()
            return redirect('profile')

@login_required
def buyP(request):
    planP = PlanPremium.objects.filter(user=request.user)
    if planP.exists():
        return redirect('error-plan')
    else:
        if request.method == 'GET':
            return render(request, 'profile/buyP.html')
        else:
            buy = PlanPremium(user=request.user,card=request.POST['card'],buyTime=timezone.now())
            buy.save()
            return redirect('profile')

@login_required
def profile(request):
    planS = PlanSolid.objects.filter(user=request.user) 
    planP = PlanPremium.objects.filter(user=request.user)
    return render(request, 'profile/profile.html', {'user': request.user,'planS': planS,'planP': planP})

@login_required
def signout(request):
    logout(request)
    return redirect('index')

@login_required
def comprar(request):
    return render(request, 'profile/comprar.html')

@login_required
def contact(request):
    return render(request, 'contact.html')
