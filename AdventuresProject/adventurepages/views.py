from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexPageView(request) :
    return render(request, 'adventurepages/index.html')

def campingPageView(request, trip_name, trip_length) :

    context = {
        "trip_name" : trip_name,
        "trip_length" : trip_length + 2,
        "places_to_visit" : ["Arenal Volcano", "Manual Antonio National Park", "Monteverde Cloud Forest"]
    } 

    return render(request, 'adventurepages/camping.html', context)   

def hikingPageView(request) :
    return HttpResponse('This is the hiking response')

def climbingPageView(request) :
    return HttpResponse('This is the climbing response')    