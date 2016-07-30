from __future__ import unicode_literals

from django.db import models
import re # for regular expressions
import bcrypt # for hashing passwords
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') # to verify email address

# Create your models here.
# Create UserManager for User model
class UserManager(models.Manager):
	def registration(self, reg):
		# pull values from inputs off of form
		first_name = reg['first_name']
		last_name = reg['last_name']
		email = reg['email']
		password = reg['password']
		confirm_password = reg['confirm_password']

		#validate inputs off of form
		if len(first_name) < 2:
			return(False, "First name must contain more than two characters")
		if not first_name.isalpha():
			return (False, "First name contain only characters from A-Z.")
		if len(last_name) < 2:
			return(False, "Last name must contain more than two characters")
		if not last_name.isalpha():
			return (False, "Last name contain only characters from A-Z.")
		if len(email) < 1:
			return (False, "Email cannot be left blank.")
		if not EMAIL_REGEX.match(email):
			return (False, "Email address is invalid.")
		if len(password) < 1:
			return(False, "Password cannot be left blank")
		if len(confirm_password) < 1:
			return(False, "You must verify your password")
		elif len(password) < 8:
			return(False, "Password must be longer than 8 characters")
		elif password != confirm_password:
			return(False, "Passwords do not match!")
		else:
			print "In else part of statement" # for testing purposes
			#hash password
			hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) #must encode password or it will throw error
			print "password hashed" # for testing purposes
			#Create user
			User.objects.create(first_name=first_name, last_name=last_name,email=email,password=hashed)
			print "user created" # for testing purposes
			return(True, "Success")

	def login(self, login_info):
		# pull input from form
		login_email = login_info['login_email']
		login_pw = login_info['login_password']
		#validate inputs
		if len(login_email) < 1 or len(login_pw) < 1:
			return(False, "Ensure you gave correct login information.")
		# look for email in DB
		try:
			print "In try email" # for testing purposes
			user = User.objects.get(email=login_email)
			if bcrypt.hashpw(login_pw.encode(), user.password.encode()) != user.password: # check password
				return(False, "Password or email incorrect.")
			print "past try password" # for testing purposes
			return(True, "Login successful!", user.first_name)
		except:
			return (False, "Email and/or password not found")

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField() # also helps to check email validation, found in docs https://docs.djangoproject.com/en/1.9/ref/models/fields/
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# Connect instance of UserManager to User model
	userManager = UserManager()
	# Re-add objects as manager
	objects = models.Manager()
