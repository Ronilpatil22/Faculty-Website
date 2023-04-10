from django.shortcuts import render

def index(request):
    return render(request, "index.html",{"var": "work"})

def research(request):
    return render(request, "research-group.html")

def students(request):
    return render(request, "student-portal.html")

def discussion(request):
    return render(request, "discussion.html")

def contact(request):
    return render(request, "contact.html")

def mywork(request):
    return render(request, "my-work.html")

def aboutme(request):
    return render(request, "about-me.html")

def creators(request):
    return render(request, "creators.html")
    

# Create your views here.
