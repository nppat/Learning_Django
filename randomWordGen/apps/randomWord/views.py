from django.shortcuts import render, redirect, HttpResponse
import random, string

# Create your views here.
def index(request):
	if ('attempt' in request.session) == False:
	# initialize the counter.  Couldnt figure this out, so I looked at Tommy Oh's views.py and learned from him
		request.session['attempt'] = 1
	return render(request, 'randomWord/index.html')

def rword(request):
	if request.method == "POST":
		request.session['rword'] =''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(14))
		# Creation of random string was found on StackOverflow.  I did find a RandomWord() module that you can install.
		# pip install RandomWord
		# it was neat and created words, nicknames, or Lorem Ipsum, but I didn't have any luck setting lenght, and dont have the time to play with it all evening
		request.session['attempt'] += 1 # add one to the counter
		return redirect('/') # redirect to the index
	else:
		return redirect('/')

# Becareful in naming things, if its a keyword in python, the program will not work correctly!