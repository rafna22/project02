from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')



def service(request):
	return render(request,'services.html')

def head(request):
	return render(request,"headerfooter.html")

def register(request):
	if request.method=="POST":
		uname=request.POST['name']
		email=request.POST['email']
		password=request.POST['password']
		image=request.FILES['image']
		check=usertab.objects.filter(email=email)
		if check:
			return render(request,'register.html',{"error":"email already taken"})
		else:
			user =usertab(username=uname,password=password,email=email,image=image)
			user.save()
			return render(request,'index.html')

	else:
		return render(request,"register.html")

def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		check=usertab.objects.filter(email=email,password=password)
		if check:
			for x in check:
				request.session['myid']=x.id
				request.session['myname']=x.username
			return render(request,'index.html',{"success":"logged in"})
		else:
			return render(request,'login.html',{"error":"invalid"})
	else:
		return render(request,'login.html')

def logout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		del request.session['myname']
		return HttpResponseRedirect('/')
	else:
		return redirect('/')



def contact(request):
	if request.method =='POST':
		name=request.POST['Name']
		email=request.POST['email']
		message=request.POST['Message']
		check= cont_tb.objects.filter(email=email)
		if check:
			return render(request,'contact.html',{"error":"email already taken"})
		else:

			data=cont_tb(name=name,email=email,message=message)
			data.save()
			return  redirect('/')
	else:
		return render(request,'contact.html')

def display(request):
	data=usertab.objects.all()
	return render(request,'display.html',{'datas':data})

def update(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		password=request.POST['password']
		regid=request.GET['regid']
		data=usertab.objects.filter(id=regid).update(username=name,email=email,password=password)
		return redirect('/display')

	else:
		regid=request.GET['regid']
		data=usertab.objects.filter(id=regid)
		return render(request,'update.html',{'data':data})

def delete(request):
	regid=request.GET['regid']
	data=usertab.objects.filter(id=regid).delete()
	return redirect('/display')