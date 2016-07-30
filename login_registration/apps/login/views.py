from django.shortcuts import render, redirect
from .models import User

# Create your views here.
# Root index route
def index(request):
	# request.session.flush()
	return render(request, "login/index.html")

#Process registration form
def process(request):
	if request.method == "POST":
		val_result = User.userManager.registration(request.POST)
		'''
		If [0] == false, some part of the validation isn't jiving, and the appropriate error message should
		be thrown to let the user know which part of the validation needs to be corrected.  The message will
		be located at val_result[1] and will display on the index.html page.
		'''
		if val_result[0] == False:
			request.session['error'] = val_result[1]
			return redirect('/')
		elif val_result[0]  == True:
			# request.session.flush()
			request.session['message'] = val_result[1]
			request.session['first_name'] = request.POST['first_name']
			return render(request, "login/success.html")

# Login
def login(request):
	if request.method == "POST":
		request.session.flush()
		print "In views login" # for testing purposes
		val_result = User.userManager.login(request.POST)
		if val_result[0] == False:
			print "False" # for testing purposes
			request.session['error'] = val_result[1]
			return redirect('/')
		elif val_result[0]  == True:
			request.session['message'] = val_result[1]
			request.session['first_name'] = val_result[2]
			return redirect('/success')

def success(request):
	return render(request, "login/success.html")
# Back button
def go_back(request):
	request.session.flush() # clear session
	return redirect('/')