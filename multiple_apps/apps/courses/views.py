from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
# root index route
def index(request):
	context = {
		'courses': Course.objects.all() # Brings in all Course objects and sets them in the context dictionary
	}
	return render(request, "courses_main/index.html", context) # passing the objects to context to access them 

# Create course and add to index.html table
def create(request):
	if request.method == "POST": # if the form method is post, create an object in Course with a name, description that is inputted by user
		Course.objects.create(course_name=request.POST.get('name_input'), description=request.POST.get('description'))
	return redirect('/') # redirect back to root with new info

# Destroy course record from DB
def destroy(request, id): # pass the id
	'''
	On index page, if form method is GET, return the course id and in redirect to destroy page,
	where there are two choice, keep or destory.  If keep, then redirect back to root, elseif destroy, delete
	data from DB on that course id and return to root
	'''
	if request.method == "GET":
		context = {
			'course': Course.objects.get(id=id)
		}
		return render(request, "courses_main/destroy.html", context)
	elif request.method == "POST":
		Course.objects.get(id=id).delete()
		print "Course Deleted" # print to terminal to ensure delete has passed
		return redirect('/')