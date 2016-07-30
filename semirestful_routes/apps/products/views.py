from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def index(request):
	context = {
		'products': Product.objects.all() # Brings in all Course objects and sets them in the context dictionary
	}
	return render(request, 'products/index.html', context)

def show(request, id):
	product = Product.objects.get(id=id)
	context = {
		'id' : id,
		'name' : product.name,
		'description' : product.description,
		'price' : product.price
	}
	return render(request, 'products/show.html', context)

def new(request):
	return render(request, 'products/new.html')

def edit(request, id):
	product = Product.objects.get(id=id)
	context = {
		'id' : id,
		'name' : product.name,
		'description' : product.description,
		'price' : product.price
	}
	return render(request, 'products/edit.html', context)

def create(request):
	if request.method == "POST":
		val_result = Product.userManager.create_product(request.POST)
		'''
		If [0] == false, some part of the validation isn't jiving, and the appropriate error message should
		be thrown to let the user know which part of the validation needs to be corrected.  The message will
		be located at val_result[1] and will display on the index.html page.
		'''
		if val_result[0] == False:
			request.session['error'] = val_result[1]
			print "create view error"
			return render(request, "products/new.html")
		elif val_result[0]  == True:
			print "create view ok"
			return redirect('/')

def update(request, id):
	if request.method == "POST":
		val_result = Product.userManager.edit(request.POST, id)
		'''
		If [0] == false, some part of the validation isn't jiving, and the appropriate error message should
		be thrown to let the user know which part of the validation needs to be corrected.  The message will
		be located at val_result[1] and will display on the index.html page.
		'''
		if val_result[0] == False:
			request.session['error'] = val_result[1]
			print "update view error" # for testing
			return redirect("products/edit/{}".format(id))
		elif val_result[0]  == True:
			print "update view ok" # for testing
			return redirect('/')

def destroy(request, id):
	if request.method == "POST":
		Product.objects.get(id=id).delete() # delete product from DB via id
		return redirect('/')





