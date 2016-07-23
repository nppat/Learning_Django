from django.shortcuts import render
from .models import User # this brings in the models from class User
# Create your views here.
# root
def index(request):
	'''
	Create into User what it is told to create
	'''
	User.objects.create(first_name="Patrick", last_name="Adamson", email="123@mail.com", password="1234")
	people = User.objects.all()
	print people # shows that User.objects.create is working
	return render(request, 'wall/index.html')