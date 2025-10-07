from django.http import HttpResponse

def home(request): 
    context = {
        "title": "Welcome to the Cloud Engineering Intern Crash Course",
        "cta_text": "Get started",
    }
    return render(request, "core/home.html", context)