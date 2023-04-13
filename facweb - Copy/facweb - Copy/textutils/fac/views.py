from django.shortcuts import render
from .models import testimonials
from.models import introduction

# Create your views here.
def index(request):
    introduction_list = introduction.objects.all()
    testimonial_list = testimonials.objects.all()
    return render(request, "index.html",{'testimonial_1': testimonial_list,'introduction':introduction_list})

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
    