from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,AthleteForm,SponsorForm
from .models import Athlete,Sponsor
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.

def index(request):
    athlete_list=Athlete.objects.all()
    sponsor_list = Sponsor.objects.all()

    return render(request,'index.html',{'athlete_list':athlete_list,'sponsor_list':sponsor_list})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = RegisterForm()

    return render(response,"register.html",{"form":form})

def logoutPage(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def athletes(request):
    athlete_list=Athlete.objects.all()
    return render(request,'athletes.html',{'athlete_list':athlete_list})

@login_required(login_url='login')
def sponsors(request):
    sponsor_list=Sponsor.objects.all()
    return render(request,'sponsors.html',{'sponsor_list':sponsor_list})


@login_required(login_url='login')
def addAthlete(request):

    
    if request.method=='POST':
        
        form = AthleteForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"athlete added successfully")
            return redirect('athletes')
    else:
        form=AthleteForm()

    context = {'form':form}

    return render(request,'addAthlete.html',context)

@login_required(login_url='login')
def addSponsor(request):

    
    if request.method=='POST':
        
        form = SponsorForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"sponsor added successfully")
            return redirect('sponsors')
    else:
        form=SponsorForm()

    context = {'form':form}

    return render(request,'addSponsor.html',context)

@login_required(login_url='login')
def athleteUpdate(request,id):
    myData = Athlete.objects.get(id=id)
    updateForm = AthleteForm(request.POST or None,instance=myData)
    if updateForm.is_valid():
        updateForm.save()
        messages.success(request,'profile updated successfully')
        return redirect('athletes')
    context={'form':updateForm}
    return render(request,'athleteUpdate.html',context)

@login_required(login_url='login')
def athleteDelete(request,id):
    data=Athlete.objects.get(id=id)
    messages.warning(request,'profile deleted successfully')
    data.delete()
    return redirect('athletes')

@login_required(login_url='login')
def sponsorDelete(request,id):
    data=Sponsor.objects.get(id=id)
    messages.warning(request,'profile deleted successfully')
    data.delete()
    return redirect('sponsors')

@login_required(login_url='login')
def sponsorUpdate(request,id):
    myData = Sponsor.objects.get(id=id)
    updateForm = SponsorForm(request.POST or None,instance=myData)
    if updateForm.is_valid():
        updateForm.save()
        messages.success(request,'profile updated successfully')
        return redirect('sponsors')
    context={'form':updateForm}
    return render(request,'sponsorUpdate.html',context)
