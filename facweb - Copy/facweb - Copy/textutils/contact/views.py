from django.shortcuts import render
from.models import contacts
from fac.models import socialmediabar
from fac.models import Navbar
from fac.models import Navbar_icon
# Create your views here.
def contact(request):
    contact_list = contacts.objects.all()
    socialmedia_list = socialmediabar.objects.all()
    Navbar_list = Navbar.objects.all()
    Navbar_icon_list = Navbar_icon.objects.all()
    return render(request, "contact.html",{'socialmedia':socialmedia_list,'contact':contact_list,'navbar':Navbar_list,'Navbar_icon':Navbar_icon_list})