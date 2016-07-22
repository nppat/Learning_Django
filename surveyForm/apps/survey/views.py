from django.shortcuts import render, redirect, HttpResponse

#CONTROLLER!

# Create your views here.
def index(request):
	return render(request, 'survey/index.html')

def process(request):
	if request.method == "POST":
		# initialize the counter.
		if ('attempt' in request.session) == False:
			request.session['attempt'] = 1
		else:
			request.session['attempt'] += 1
		# Set up sessions and pull data from form
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comments'] = request.POST['comments']
		return redirect('/result')
	else:
		return redirect('/')

def result(request):
	build = {
		'name': request.session['name'],
		'location': request.session['location'],
		'language': request.session['language'],
		'comments': request.session['comments'],
	}
	return render(request, 'survey/result.html', build)