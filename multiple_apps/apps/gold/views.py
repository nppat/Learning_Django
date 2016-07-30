from django.shortcuts import render, redirect
from django.contrib import messages # for messaging, like Flash messages
import random # for creating random integers for the game
# Create your views here.
# root route
def index(request):
	if ('gold_counter' in request.session) == False:
			request.session['gold_counter'] = 0
	else:
		request.session['gold_counter']
	return render(request, "gold/index.html")
# process when the form buttons are pushed
def process_gold(request):
	# Set up sessions and pull data from form
	value = request.POST['action']
	if request.method == "POST":
		if value == "farm":
			# make random amount of gold pass into counter (10-20)
			random_gold = random.randrange(10,20) # get random int, set into variable
			print random_gold	# print to terminal to see if working correctly
			request.session['gold_counter'] += random_gold # set random int into session
			messages.success(request, "You earned " + str(random_gold) + " gold !") # messaging format, convert int to str
		elif value == "cave":
			# make random amount of gold pass into counter
			# 5-10
			random_gold = random.randrange(5,10)
			print random_gold
			request.session['gold_counter'] += random_gold
			messages.success(request, "You earned " + str(random_gold) + " gold !")
		elif value == "house":
			# make random amount of gold pass into counter
			# 2-5
			random_gold = random.randrange(2,5)
			print random_gold
			request.session['gold_counter'] += random_gold
			messages.success(request, "You earned " + str(random_gold) + " gold !")
		elif value == "casino":
			# make random amount of gold pass into counter
			# -50 - +50
			random_gold = random.randrange(-50,50)
			print random_gold
			request.session['gold_counter'] += random_gold
			if random_gold > 0:
				messages.success(request, "You gambled and won " + str(random_gold) + " gold !")
			else:
				messages.warning(request, "You gambled and lost " + str(random_gold) + " gold!")
	return redirect('/')

def reset(request):
	print "RESET" # test the form to see if working on button press
	if request.method == "POST": # if method is post
		try: # try to delete the session key of gold_counter
			del request.session['gold_counter']
		except:
			pass
		return redirect('/') # redirect to root with cleared session
	else:
		return redirect('/')