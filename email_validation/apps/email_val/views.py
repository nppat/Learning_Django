from django.shortcuts import render, redirect, HttpResponse
from .models import Email, UserManager

# Create your views here.
# root route
def index(request):
	context = {
		'emails': Email.objects.all() # set context to be able to view all emails in Email object
	}
	return render(request, 'email_val/index.html', context) #show emails on index.html

def submit(request):
	'''
		This checks to see if there is a valid email address presented through the input on index.html.
		When there is not a valid address, or the input is left empty, there is a message returned to the 
		user that states either the address is invalid or the email input is blank.  When successful, the
		user is informed as such.  I had to reference Tommy and Marynn github, becuase the messaging system 
		I was trying to set up did not work at all.  I also found a build-in email validator in the Django Docs,
		but I think the course wants to use user-built methods first, and then move on to the built-in methods.
	'''
	if request.method == "POST":
		val_result = Email.userManager.email_val(request.POST['email_input'])
		if val_result[0] == False:
			request.session['error'] = val_result[1]
			return redirect('/')
		elif val_result[0] == True:
			Email.objects.create(email=request.POST['email_input'])
			request.session['message'] = val_result[1]
			return redirect('/')
	else:
		return redirect('/')
