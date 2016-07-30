from __future__ import unicode_literals

from django.db import models

# Create UserManager()
class UserManager(models.Manager):
	def create_product(self, product):
		# get inputs from form
		name = product['name']
		description = product['description']
		price = product['price']

		# validate input
		if len(name) < 1 or len(description) < 1 or len(price) < 1:
			return(False, "Please fill out all parts of the form.")
		elif len(description) > 1000:
			return(False, "Please keep description under 1000 characters.")
		else:
			Product.objects.create(name=name, description=description, price=price)
			return(True, "New product created!")
	def edit(self, update, id):
		# get updated input from user
		name = update['name']
		description = update['description']
		price = update['price']
		# get id for product
		update = Product.objects.get(id=id)
		# Validate input
		if len(name) < 1 or len(description) < 1 or len(price) < 1:
			return(False, "Please fill out all parts of the form.")
		elif len(description) > 1000:
			return(False, "Please keep description under 1000 characters.")
		else:
			# set update var to DB var and update the DB with .save()
			update.name = name
			update.description = description
			update.price = price
			update.save() # save the updated product data
			return (True, "Updated successfully.")

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=1000)
	price = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	#connect to UserManager
	userManager = UserManager()
	#ORM
	objects = models.Manager()