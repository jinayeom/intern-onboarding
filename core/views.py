from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse
from roadmap.models import Roadmap  
from django.template.loader import get_template, TemplateDoesNotExist

TOPICS = [
        {"title": "Setting up your Development Environment", "slug":"ssh-dev-env"},
        {"title": "Creating a Branch", "slug":"creating-branch"},
        {"title": "How to Compile your Code", "slug":"compile-code"},
    ]

def home(request): 
    roadmaps = Roadmap.objects.order_by("title")  
    
    context = {
        "title": "Welcome to the Cloud Engineering Intern Crash Course",
        "cta_text": "Get started",
        "roadmaps": roadmaps, 
    }
    return render(request, "core/home.html", context)

def modules_index(request):
    topics = sorted(TOPICS, key=lambda t: t["title"].lower())
    return render(request, "core/modules/index.html", {"topics": TOPICS})

def module_detail(request, slug):
    topics = TOPICS
    module = next((t for t in topics if t.get("slug") == slug), None)

    if not module:
        raise Http404("Module not found")

    # Try to find a matching template file for the module slug
    template_name = f"core/modules/pages/{slug}.html"
    fallback_template = "core/modules/detail.html"

    # Absolute path check ensures template file actually exists
    try:
        get_template(template_name)
        chosen_template = template_name
    except TemplateDoesNotExist:
        chosen_template = fallback_template

    module_url = reverse("module-detail", kwargs={"slug": slug})

    context = {
        "module": module,
        "module_url": module_url, 
    }

    return render(request, chosen_template, context)
