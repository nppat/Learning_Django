from django.shortcuts import render ,HttpResponse # import HttpResponse
import time # from python time
# THIS IS THE CONTROLLER IN M-V-C

# Create your views here.

# Not sure how to get real local, seems to be off of UTC and seconds from.  But I need to move on.  The main concept of building an app within the Django model is understood.
def index(request):
	local = time.asctime( time.localtime(time.time()) ) # found on http://www.tutorialspoint.com/python/python_date_time.htm
	morris_day_and_the_mf_time = {
		"current_date_time": local,
	}
	return render(request, 'timedisplay/index.html', morris_day_and_the_mf_time)