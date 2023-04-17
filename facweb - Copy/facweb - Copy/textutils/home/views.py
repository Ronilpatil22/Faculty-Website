from django.shortcuts import render
from .models import testimonials
from.models import introductions
from.models import newsletter
from fac.models import socialmediabar
from fac.models import Navbar
from fac.models import Navbar_icon
# Create your views here.

def index(request):
    introduction_list = introductions.objects.all()
    testimonial_list = testimonials.objects.all()
    newsletter_list = newsletter.objects.all()
    socialmedia_list = socialmediabar.objects.all()
    Navbar_list = Navbar.objects.all()
    Navbar_icon_list = Navbar_icon.objects.all()
    return render(request, "index.html",{'testimonial_1': testimonial_list,'introduction':introduction_list,'newsletter':newsletter_list,'socialmedia':socialmedia_list,'navbar':Navbar_list,'Navbar_icon':Navbar_icon_list})