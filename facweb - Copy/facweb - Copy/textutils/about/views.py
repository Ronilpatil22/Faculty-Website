from django.shortcuts import render
from fac.models import socialmediabar
from fac.models import Navbar
from fac.models import Navbar_icon
# Create your views here.

def aboutme(request):
    socialmedia_list = socialmediabar.objects.all()
    Navbar_list = Navbar.objects.all()
    Navbar_icon_list = Navbar_icon.objects.all()
    return render(request, "about-me (2).html",{'socialmedia':socialmedia_list,'navbar':Navbar_list,'Navbar_icon':Navbar_icon_list})