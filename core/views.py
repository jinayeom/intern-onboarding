from django.http import HttpResponse
from django.shortcuts import render
from roadmap.models import Roadmap  

def home(request): 
    roadmaps = Roadmap.objects.order_by("title")  
    
    context = {
        "title": "Welcome to the Cloud Engineering Intern Crash Course",
        "cta_text": "Get started",
        "roadmaps": roadmaps, 
    }
    return render(request, "core/home.html", context)