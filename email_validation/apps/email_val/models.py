from __future__ import unicode_literals
from django.db import models
import re # for regular expressions
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') # to verify email address

# Create your models here.
class UserManager(models.Manager):
	def email_val(self, email):
		# check for email address input, and if none, throw out an error message
		if len(email) < 1:
			return(False, "Email cannot be left blank.")
		elif not EMAIL_REGEX.match(email):
			return(False, "Email address is invalid.")
		else:
			return(True, "The email address you entered, {}, is a valid email address!  Thank You!".format(email))			
class Email(models.Model):
	email = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userManager = UserManager()
	objects = models.Manager()

