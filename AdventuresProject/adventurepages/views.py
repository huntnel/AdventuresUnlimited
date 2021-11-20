from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexPageView(request) :
    return render(request, 'adventurepages/index.html')

def campingPageView(request) :
    return render(request, 'adventurepages/camping.html')   

def hikingPageView(request) :
    return render(request, 'adventurepages/hiking.html')
   