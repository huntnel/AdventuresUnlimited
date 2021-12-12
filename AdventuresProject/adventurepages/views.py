from django.shortcuts import render
from django.http import HttpResponse
from .models import Hike, Camp

# Create your views here.

def indexPageView(request) :
    return render(request, 'adventurepages/index.html')

def aboutPageView(request) :
    return render(request, 'adventurepages/about.html')

def campingPageView(request) :
    data = Camp.objects.all()
    context = {
        'camps' : data
    }
    return render(request, 'adventurepages/camping.html', context)   

def hikingPageView(request) :
    return render(request, 'adventurepages/hiking.html')

def createHikePageView(request) :
    return render(request, 'adventurepages/createhike.html')

def createCampPageView(request) :
    return render(request, 'adventurepages/camping.html')

def updateHikePageView(request) :
    return render(request, 'adventurepages/updatehike.html')

def updateCampPageView(request) :
    return render(request, 'adventurepages/updatecamp.html')

def deleteHikePageView(request) :
    return render(request, 'adventurepages/deletehike.html')

def deleteCampPageView(request) :
    return render(request, 'adventurepages/deletecamp.html')

def storeHikePageView(request) :
        #Check to see if the form method is a get or post
    if request.method == 'POST':

        #Create a new employee object from the model (like a new record)
        new_hike = Hike()
        
        #Store the data from the form to the new object's attributes (like columns)
        new_hike.hikename = request.POST.get('hike_name')
        new_hike.elevationgain = int(request.POST.get('elevation_gain'))
        new_hike.length = float(request.POST.get('length'))
        new_hike.description = request.POST.get('description')
        new_hike.bathroom = bool(request.POST.get('bathroom'))
        new_hike.potablewater = bool(request.POST.get('water'))
        # new_hike.firepits = request.POST.get('fire')
        new_hike.address = request.POST.get('address')
        new_hike.city = request.POST.get('city')
        new_hike.state = request.POST.get('state')
        new_hike.zipcode = int(request.POST.get('zip'))
        new_hike.difficulty = request.POST.get('difficulty')
                
        #Save the employee record
        new_hike.save()
    return render(request, 'adventurepages/hiking.html')

def storeCampPageView(request) :
    return render(request, 'travelpages/storecamp.html')
   