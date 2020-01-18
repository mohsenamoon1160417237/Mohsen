from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from products.models import Product



def home(request):
	
	products = Product.objects
	return render(request , 'accounts/home.html' , {'products':products})

def signup(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request , 'accounts./signup.html' , {'error':'The account has been taken'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'] , password = request.POST['password1'])
				return redirect('home')
		else:
			return render(request , 'accounts/signup.html' , {'error':'The passwords must match'})
	else:
		return render(request , 'accounts/signup.html')


def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username = request.POST['username'] ,password = request.POST['password'])
		if user is not None:
			auth.login(request , user)
			return redirect('home')
		else:
			return render(request , 'accounts/login.html' , {'error':'Wrong username or password'})

	else:
		return render(request , 'accounts/login.html')



def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')



