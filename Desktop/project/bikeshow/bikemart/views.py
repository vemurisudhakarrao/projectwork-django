from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Registration
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request,'bmtl/home.html')

def about(request):
	return render(request,'bmtl/about.html')

def latest(request):
	return render(request,'bmtl/latestbikes.html')

def reg(request):
	if request.method == "POST":
		t = Registration(request.POST)
		# print('hi')
		if t.is_valid():
			# print('hello')
			t.save()
			return redirect('/lg')
	t = Registration()
	return render(request,'bmtl/reg.html',{'y':t})



def loginView(request):
	return render(request,'bmtl/login.html')

@login_required
def LogoutView(request):
	return render(request,'bmtl/logout.html')

@login_required
def booknow(request):
	return render(request,'bmtl/booknow.html')

@login_required
def booktvs(request):
	return render(request,'bmtl/tvs.html')







