from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'turtles/index.html')

def show(request, color=None):
	tmnt = "turtles/img/turtles/" # set tmnt = to first part of img path, less typing
	if not color:
		tmnt += "tmnt.png"
	elif color.lower() == "blue": # using color.lower() normailizes the data, as shown in the lecutre.  BLUE = blue for ex.
		tmnt += "leonardo.jpg" # add rest of img path for specific color
	elif color.lower() == "red":
		tmnt += "raphael.jpg"
	elif color.lower() == "purple":
		tmnt += "donatello.jpeg"
	elif color.lower() == "orange":
		tmnt += "michelangelo.jpg"
	else:
		tmnt += "notapril.jpg"
	# Contect = dictionary will set what we are going to show on index.html.  This is how we pass from here to there.
	context = {
			'tmnt': tmnt
		}
	return render(request, 'turtles/index.html', context)