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

def modules_index(request): 
    topics = [
        {"title": "Setting up your Development Environment", "slug":"ssh-dev-env"},
        {"title": "Creating a Branch"},
        {"title": "How to Compile your Code"},
    ]
    topics = sorted(topics, key=lambda t: t["title"].lower())
    return render(request, "core/modules/index.html", {"topics": topics})

