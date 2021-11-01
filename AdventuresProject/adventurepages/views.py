from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexPageView(request) :
    sOutput = '<html><head><title>My Title</title></head><body><p style="color:red;"><b>one</b></p><p style="color:blue;">two</p><p style="font-size:50px;">three</p><ul><li>A</li><li>B</li><li>C</li></ul></body></html>'
    return HttpResponse(sOutput)

def campingPageView(request, trip_name) :
    sOutput = sOutput = '<html><head><title>My Title</title></head><body><p>Welcome to ' + trip_name + '</p></body></html>'
    return HttpResponse(sOutput)

def hikingPageView(request) :
    return HttpResponse('This is the hiking response')

def climbingPageView(request) :
    return HttpResponse('This is the climbing response')    