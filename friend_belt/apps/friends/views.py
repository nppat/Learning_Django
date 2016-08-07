from django.shortcuts import render, redirect
from django.contrib import messages # for messages
from .models import User, Friend, Favorite

# Create your views here.
def index(request):
	return render(request, 'friends/index.html')

# Login
def login(request):
	if request.method == "POST":
		print "In views login" # for testing purposes
		val_result = User.userManager.login(request.POST)
		if val_result[0] == False:
			print "No Login" # for testing purposes
			for error in val_result[1]: # error messaging
				messages.error(request, error)
			return redirect('/')
		else:
			val_result[0]  == True
			print "good login"
			request.session['name'] = val_result[2] # [2] contains user.name
			request.session['user_id'] = val_result[3] # [3] contains. user.id
			request.session['status'] = True # set session status so we know if user is logged in or not
			return redirect(dashboard)

# Register
def register(request):
	if request.method == "POST":
		val_result = User.userManager.registration(request.POST)
		'''
		If [0] == false, some part of the validation isn't jiving, and the appropriate error message should
		be thrown to let the user know which part of the validation needs to be corrected.  The message will
		be located at val_result[1] and will display on the index.html page.
		'''
		if val_result[0] == False:
			print "register not good!"
			for error in val_result[1]: # error messaging
				messages.error(request, error)
			return redirect('/')
		else:
			val_result[0]  == True
			# request.session.flush()
			print "register good!"
			messages.success = (request, val_result[1])
			return redirect('/')
	else:
		return redirect('/')

# User Dashboard
def dashboard(request):
	user_id = request.session['user_id']
	friend = Friend.objects.all()
	context = {
		'friends' : friend,
		'non_friends' : User.objects.all().exclude(id=request.session['user_id'])
	}
	return render(request, 'friends/dashboard.html', context)

# User profile
def user(request, id):
	if ('status' in request.session): # ensure user is logged in
		user = User.objects.get(id=id)
		context = {
			'user' : user,
		}
		return render(request, 'friends/profile.html', context)
	else:
		return redirect('/') # go log in

# Add friend to Friends List
def add_friend(request, user_id):
	if ('status' in request.session): # ensure user is logged in
		if request.method == "POST":
			val_result = Friend.friendManager.friend_list(request.POST, user_id) # adds per user id
			if val_result[0] == False:
				print "add friend not good!"
				messages.error(request, val_result[1])
				return render(request, 'friends/dashboard.html')
			else:
				val_result[0]  == True
				print "add friend good!"
				messages.success = (request, val_result[1])
				return render(request, 'friends/dashboard.html')
	else:
		return redirect('/') # go and log in!
# Logout
def logout(request):
	if ('status' in request.session):
		request.session.flush()
		return redirect('/')
	else:
		return redirect('/')




