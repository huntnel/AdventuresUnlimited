from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexPageView(request) :
    return HttpResponse('This is the index response')

def campingPageView(request) :
    return HttpResponse('This is the camping response')

def hikingPageView(request) :
    return HttpResponse('This is the hiking response')

def climbingPageView(request) :
    return HttpResponse('This is the climbing response')    