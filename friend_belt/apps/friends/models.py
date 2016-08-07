from __future__ import unicode_literals

from django.db import models

import re # for regular expressions
import bcrypt # for hashing passwords
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') # to verify email address

# Create managers for phat models and skinny views
class UserManager(models.Manager):
	def registration(self, reg):
		# pull values from inputs off of form
		name = str(reg['name'])
		alias = str(reg['alias'])
		email = reg['email']
		password = reg['password']
		confirm_password = reg['confirm_pw']
		date_of_birth = reg['dob']
		errors = [] # hold error messages

		#validate inputs off of form
		if len(name) < 2 or len(alias) < 2:
			errors.append("Must contain more than two characters")
		if str.isalpha(str(reg['name'].replace(' ', ''))) != True:
			errors.append("Name must contain only characters from A-Z.")
		if len(email) < 1:
			errors.append("Email cannot be left blank.")
		if not EMAIL_REGEX.match(email):
			errors.append("Email address is invalid.")
		# Check to see if user already has registered the email address
		try:
			if User.objects.get(email=email):
				errors.append('Email address already exist!')
		except:
			pass
		if len(password) < 1:
			errors.append("Password cannot be left blank")
		if len(confirm_password) < 1:
			errors.append("You must verify your password")
		elif len(password) < 8:
			errors.append("Password must be longer than 8 characters")
		elif password != confirm_password:
			errors.append("Passwords do not match!")
		if errors: # if errors exist, send them to the errors list
			return (False, errors)
		else:
			print "In else part of statement" # for testing purposes
			#hash password
			hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) #must encode password or it will throw error
			print "password hashed" # for testing purposes
			#Create user
			User.objects.create(name=name, alias=alias, email=email, password=hashed, date_of_birth=date_of_birth)
			print "user created" # for testing purposes
			return(True, "Success!  You can login now.")

	def login(self, login):
		# pull input from form
		login_email = login['login_email']
		login_pw = login['login_password']
		errors = [] # for holding error messages
		#validate inputs
		if len(login_email) < 1 or len(login_pw) < 1:
			errors.append("Ensure you gave correct login information.")
		# look for email in DB
		try:
			print "In try email" # for testing purposes
			user = User.objects.get(email=login_email)
			if bcrypt.hashpw(login_pw.encode(), user.password.encode()) != user.password: # check password
				return(False, "Password or email incorrect.")
			print "past try password" # for testing purposes
		except:
			errors.append("Email and/or password not found")
		if errors:
			return (False, errors)
		else:
			return (True, "Login successful!", user.name, user.id)

class FriendManager(models.Manager):
	def friend_list(self, friend, user_id):
		# get friend information
		friend_id = friend['hidden_id']
		friend_name = friend['hidden_name']
		friend_alias = friend['hidden_alias']
		errors = []
		try:
			print ('########### In models friend_list try ##############')
			print friend_id, friend_name, friend_alias
			# Friend.objects.create(name=friend_name, alias=friend_alias, id=friend_id, user_id=user_id)
			Friend.objects.create(name=friend_name, alias=friend_alias, id=friend_id, user_id=user_id)
			print("######### Friend Created ###########")
			return(True, "Friend Added")
		except:
			return(False, "Friend not added")
		return(friend_query)
# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100)
	alias = models.CharField(max_length=100)
	email = models.EmailField() # also helps to check email validation, found in docs https://docs.djangoproject.com/en/1.9/ref/models/fields/
	password = models.CharField(max_length=255) # will store hashed password
	date_of_birth = models.DateField() # store birthday
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# Connect instance of UserManager to User model
	userManager = UserManager()
	# Re-add objects as manager
	objects = models.Manager()

class Friend(models.Model):
	name = models.CharField(max_length=100)
	alias = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user_id = models.ForeignKey(User)
	# Connect instance of UserManager to User model
	friendManager = FriendManager()
	# Re-add objects as manager
	objects = models.Manager()
	
class Favorite(models.Model):
	user_id = models.ForeignKey(User)
	friend_id = models.ForeignKey(Friend)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)