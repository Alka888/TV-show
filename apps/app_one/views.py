from django.shortcuts import render, redirect
from . models import Tvshow
from django.contrib import messages


def index(request):
    content = {
        "Tvshow": Tvshow.objects.all()
    }
    return render(request, 'app_one/index.html',content)
#showing the first page from index.html


def create(request):
	errors = Tvshow.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
	if len(errors) > 0:
		# if the errors dictionary contains anything, loop through each key-value pair and make a flash message
		for key, value in errors.items():
			messages.error(request, value)
		# redirect the user back to the form to fix the errors
		return redirect('/')
	else:
		title = request.POST['title']
		network = request.POST['network']
		desc = request.POST['desc']
		release_date = request.POST['release_date']
		New_show = Tvshow.objects.create(title=title, network=network,description=desc, release_date=release_date)
		print(New_show.id)
		return redirect('/show/' + str(New_show.id))
#when we push the create button, this button aftomaticly redirect us to Show/show_id page- TV Show 2,  with info about the TV Show


def showdet(request, show_id):
    content = {
        "Tvshow":  Tvshow.objects.get(id=show_id)
    }
    eshow = Tvshow.objects.get(id=show_id)
    return render(request, 'app_one/read_one.html', content)
#this function showing us the TV Show page, second one.

def showedit(request, show_id):
    content = {
        "Tvshow":  Tvshow.objects.get(id=show_id)
    }
    return render(request, 'app_one/update.html', content)
#this function showing us the third page, where we have All TV Shows in order. with delete edit and show menu.

def shows(request):
    content = {
        "Tvshow": Tvshow.objects.all()
    }
    return render(request, 'app_one/readall.html', content)
#this function happens when we go through the show link,
# and it is redirect us to previous page, where we have info about all shows(page number two - TV Show 2) 

def edit_show(request, show_id):
	tempshow = Tvshow.objects.get(id=show_id)
	errors = Tvshow.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
	if len(errors) > 0:
		# if the errors dictionary contains anything, loop through each key-value pair and make a flash message
		for key, value in errors.items():
			messages.error(request, value)
		# redirect the user back to the form to fix the errors
		return redirect('/show/'+ str(tempshow.id)+ '/edit')
	else:
		tempshow.title = request.POST['title']
		tempshow.network = request.POST['network']
		tempshow.description = request.POST['desc']
		tempshow.release_date = request.POST['release_date']
		tempshow.save()
		return redirect('/show/' + str(tempshow.id))
#this function editing the info that we have on list on the third page, when we hit this button we go to the Edit Show page, where we can update the info.
	
def delete_show(request, show_id):
	this_show = Tvshow.objects.get(id=show_id)
	this_show.delete()
	return redirect('/shows')
#this function deleting the info 


	
