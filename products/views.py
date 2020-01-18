from django.shortcuts import render , redirect , get_object_or_404
from .models import Product
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.FILES['icon'] and request.FILES['image'] and request.POST['url']:
			product = Product()
			product.title = request.POST['title']
			product.body = request.POST['body']

			if request.POST['url'].startswith('https://') or request.POST['url'].startswith('http://'):
				product.url = request.POST['url']
			else:
				product.url = 'http://' + request.POST['url']

			product.icon = request.FILES['icon']
			product.image = request.FILES['image']
			product.hunter = request.user
			product.pub_date = timezone.datetime.now()
			product.save()
			return redirect('/products/' + str(product.id))

		else:
			return render(request , 'products/create.html' , {'error':'All fields are necessary'})
	else:
		return render(request , 'products/create.html')



def details(request , product_id):
	product = get_object_or_404(Product , pk = product_id)
	return render(request , 'products/details.html', {'product':product})
	

@login_required
def upvote(request , product_id):
	if request.method == 'POST':
		product = get_object_or_404(Product , pk = product_id)
		product.votes_total += 1
		product.save()
		return redirect('/products/' + str(product.id))

