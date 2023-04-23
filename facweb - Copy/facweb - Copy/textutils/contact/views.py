from django.shortcuts import render
from.models import contacts
from fac.models import socialmediabar
from fac.models import Navbar
from fac.models import Navbar_icon
from .models import getintouch_details
from fac.models import socialmediabarmessage
# Create your views here.
def contact(request):
    contact_list = contacts.objects.all()
    socialmedia_list = socialmediabar.objects.all()
    Navbar_list = Navbar.objects.all()
    Navbar_icon_list = Navbar_icon.objects.all()
    socialmediabarmessage_list = socialmediabarmessage.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact_message=getintouch_details(Name=name,Email=email,Subject=subject,Message=message)
        contact_message.save()
        return render(request, "contact.html",{'socialmedia':socialmedia_list,'contact':contact_list,'navbar':Navbar_list,'Navbar_icon':Navbar_icon_list,'socialmediabarmessage':socialmediabarmessage_list})
    else:
        return render(request, "contact.html",{'socialmedia':socialmedia_list,'contact':contact_list,'navbar':Navbar_list,'Navbar_icon':Navbar_icon_list,'socialmediabarmessage':socialmediabarmessage_list})
    

